from flask import Flask, request, jsonify, session
import psycopg2
import os
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'insecure_secret_key_123'  # Clave insegura

# Configuración vulnerable - sin MFA
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'snowflake-db'),
    'database': 'snowflake_sim',
    'user': 'admin',
    'password': os.getenv('DB_PASSWORD', 'Admin123'),  # Contraseña por defecto
    'port': 5432
}

def get_db_connection():
    """Conexión a la base de datos sin autenticación robusta"""
    return psycopg2.connect(**DB_CONFIG)

@app.route('/login', methods=['POST'])
def login():
    """Endpoint de login sin MFA"""
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    # Autenticación básica sin MFA
    if username == 'admin' and password == 'Admin123':
        session['user'] = username
        session['logged_in'] = True
        log_event('LOGIN_SUCCESS', username, request.remote_addr)
        return jsonify({'status': 'success', 'message': 'Login exitoso (sin MFA)'})
    
    log_event('LOGIN_FAILED', username, request.remote_addr)
    return jsonify({'status': 'error', 'message': 'Credenciales inválidas'}), 401

@app.route('/data', methods=['GET'])
def get_sensitive_data():
    """Endpoint que devuelve datos sensibles"""
    if not session.get('logged_in'):
        return jsonify({'error': 'No autenticado'}), 401
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM customer_data LIMIT 100")
        data = cur.fetchall()
        cur.close()
        conn.close()
        
        log_event('DATA_ACCESS', session['user'], request.remote_addr)
        return jsonify({'data': data, 'count': len(data)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/query', methods=['POST'])
def execute_query():
    """Endpoint para ejecutar consultas SQL (vulnerable a inyección)"""
    if not session.get('logged_in'):
        return jsonify({'error': 'No autenticado'}), 401
    
    query = request.json.get('query', '')
    
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(query)  # Vulnerable a SQL injection
        data = cur.fetchall()
        cur.close()
        conn.close()
        
        log_event('QUERY_EXECUTED', session['user'], request.remote_addr, query)
        return jsonify({'results': data})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def log_event(event_type, user, ip, details=''):
    """Registro de eventos de seguridad"""
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'event_type': event_type,
        'user': user,
        'ip': ip,
        'details': details
    }
    print(f"[SECURITY_LOG] {json.dumps(log_entry)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)  # Debug activado - inseguro
