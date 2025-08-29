import requests
import uuid
import base64
import re

BASE_URL = "https://example.htb"  # <-- aquí pones el dominio del reto

def obtener_booking():
    # 1. Hacer GET a la página que tiene el parámetro data
    r = requests.get(f"{BASE_URL}/pay.php?data=test123")
    
    # Simulamos extraer `data` de la URL (en la práctica lo parseas de r.url o r.text)
    match = re.search(r"data=([a-zA-Z0-9]+)", r.url)
    if not match:
        raise Exception("No se encontró parámetro data en la URL")
    
    data_param = match.group(1)
    
    # 2. Convertirlo en Base64
    booking = base64.b64encode(f"{BASE_URL}/pay.php?data={data_param}".encode()).decode()
    return booking

def enviar_post(booking):
    # 3. Enviar POST con uuid dinámico y booking generado
    payload = {
        "ttcc": "1111 2222 3333 4444",
        "bk_name": "Banco Demo",
        "cname": "Usuario Demo",
        "cmexp": "12",
        "cyexp": "2027",
        "csc": "123",
        "cc": "999999999",
        "tel": "123456789",
        "city": "HTB",
        "address": "Hack Street 123",
        "mail": "demo@htb.local",
        "uuid": str(uuid.uuid4()),
        "booking": booking,
        "u": "",
        "p": ""
    }

    r = requests.post(f"{BASE_URL}/api/api.php?a=nu", data=payload)
    print("Respuesta:", r.status_code, r.text[:200])

if __name__ == "__main__":
    booking = obtener_booking()
    enviar_post(booking)
