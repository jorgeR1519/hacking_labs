import requests
from colorama import Fore, Style, init

# Inicializar colorama (para compatibilidad con Windows)
init()

url = "https://portalpagosmov.com/api/api.php?a=nu"
headers = {
    "Host": "portalpagosmov.com",
    "Content-Length": "329",
    "Sec-Ch-Ua-Platform": "\"Android\"",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Mobile Safari/537.36",
    "Accept": "*/*",
    "Sec-Ch-Ua": "\"Not;A=Brand\";v=\"99\", \"Google Chrome\";v=\"139\", \"Chromium\";v=\"139\"",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Sec-Ch-Ua-Mobile": "?1",
    "Origin": "https://portalpagosmov.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "es-ES,es;q=0.9",
    "Priority": "u=1, i",
    "Connection": "keep-alive"
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
    "uuid": "4036345083",
    "booking": "aHR0cHM6Ly9wb3J0YWxwYWdvc21vdi5jb20vcGF5LnBocD9kYXRhPWJqUndVRk5UWm1aWk0xRjNhUzgxVTBoclYzWXZaejA5",
    "u": "",
    "p": ""
}

for i in range(1000):
    try:
        response = requests.post(url, headers=headers, data=data, timeout=10)
        status = response.status_code
        
        if status == 200:
            print(f"{Fore.GREEN}[{i+1}/1000] Status: {status} - OK{Style.RESET_ALL}")
        elif status == 404:
            print(f"{Fore.RED}[{i+1}/1000] Status: {status} - Not Found{Style.RESET_ALL}")
        elif status == 403:
            print(f"{Fore.YELLOW}[{i+1}/1000] Status: {status} - Forbidden{Style.RESET_ALL}")
        elif status == 500:
            print(f"{Fore.RED}[{i+1}/1000] Status: {status} - Server Error{Style.RESET_ALL}")
        else:
            print(f"{Fore.BLUE}[{i+1}/1000] Status: {status} - Unknown{Style.RESET_ALL}")
            
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}[{i+1}/1000] Error: {str(e)}{Style.RESET_ALL}")