"""Comprueba exclusivamente los dos servicios locales del laboratorio."""
import json
import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import ProxyHandler, Request, build_opener

OPENER = build_opener(ProxyHandler({}))


def read_info(base):
    with OPENER.open(base + '/?format=json', timeout=5) as response:
        return json.load(response)


def verify(port, expected):
    base = f'http://127.0.0.1:{port}'
    before = read_info(base)
    assert before['lab'] == 'php2shell-lab', 'Servicio equivocado'
    assert before['php'] == expected, f'Version inesperada: {before}'
    assert before['sapi'] == 'apache2handler', 'Se requiere mod_php'
    assert before['memory_limit'] == '16M', 'Limite de memoria inesperado'
    print(f'{base}: PHP {expected}, mod_php, PID {before["pid"]}')
    try:
        with OPENER.open(Request(base + '/oom.php', data=b''), timeout=10) as response:
            raise AssertionError(f'OOM respondio HTTP {response.status}; revisar logs')
    except HTTPError as exc:
        if exc.code != 500:
            raise
        print('  HTTP 500 observado; revisar logs para confirmar OOM.')
    except (URLError, ConnectionError, TimeoutError) as exc:
        print(f'  Conexion interrumpida ({exc}); revisar logs del worker.')
    for attempt in range(10):
        try:
            after = read_info(base)
            assert after['php'] == expected
            print(f'  Servicio disponible despues del ejercicio; PID {after["pid"]}.')
            return
        except (URLError, ConnectionError, TimeoutError):
            if attempt == 9:
                raise
            time.sleep(1)


if __name__ == '__main__':
    try:
        verify(8086, '8.2.34')
        verify(8087, '8.2.35')
    except (AssertionError, OSError, ValueError) as exc:
        print(f'FALLO: {exc}', file=sys.stderr)
        sys.exit(1)
    print('Verificacion del entorno terminada. No demuestra explotacion de los CVE.')
