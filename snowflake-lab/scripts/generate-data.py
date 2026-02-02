#!/usr/bin/env python3
"""
Generador de datos de prueba para el laboratorio
"""
import psycopg2
import random
from faker import Faker
import sys

def generate_test_data(num_records=1000):
    """Genera datos de prueba para simulación"""
    
    fake = Faker()
    
    try:
        conn = psycopg2.connect(
            host="snowflake-db",
            database="snowflake_sim",
            user="admin",
            password="Admin123",
            port=5432
        )
        
        cur = conn.cursor()
        
        print(f"[*] Generando {num_records} registros de prueba...")
        
        for i in range(num_records):
            # Insertar datos de clientes
            cur.execute("""
                INSERT INTO customer_data 
                (name, email, phone, credit_card, ssn, address)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (
                fake.name(),
                fake.email(),
                fake.phone_number(),
                fake.credit_card_number(),
                fake.ssn(),
                fake.address()
            ))
            
            # Insertar registros financieros
            if i % 3 == 0:
                cur.execute("""
                    INSERT INTO financial_records 
                    (customer_id, transaction_date, amount, account_number, routing_number, bank_name)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, (
                    random.randint(1, 100),
                    fake.date_this_year(),
                    round(random.uniform(-5000, 10000), 2),
                    fake.bban(),
                    fake.swift11(),
                    fake.company()
                ))
            
            if i % 100 == 0:
                print(f"[*] Progreso: {i}/{num_records}")
                conn.commit()
        
        conn.commit()
        cur.close()
        conn.close()
        
        print(f"[+] Datos generados exitosamente: {num_records} registros")
        
    except Exception as e:
        print(f"[-] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    generate_test_data(5000)  # Generar 5000 registros
