
import json
from http.cookiejar import CookieJar
from urllib.request import build_opener, HTTPCookieProcessor

TARGETS = {
    "PHP 8.2.34": "http://127.0.0.1:8086",
    "PHP 8.2.35": "http://127.0.0.1:8087",
}


def test_session(url):
    cookies = CookieJar()
    client = build_opener(HTTPCookieProcessor(cookies))

    def request():
        with client.open(url + "/sessions.php", timeout=5) as response:
            return json.load(response)

    first = request()
    second = request()

    return (
        first["visitas"] == 1
        and second["visitas"] == 2
        and first["session_active"]
        and second["session_active"]
    )


for version, url in TARGETS.items():
    try:
        result = test_session(url)
        print(f"{version}: {'PASS' if result else 'FAIL'}")
    except Exception as exc:
        print(f"{version}: ERROR - {exc}")
