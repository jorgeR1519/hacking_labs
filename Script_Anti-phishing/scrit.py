#!/usr/bin/env python3
# USAR SOLO EN SERVIDORES/ENTORNOS DONDE TENGAS PERMISO EXPLÍCITO.

import argparse, time, threading, random
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import uuid

def send(session, url, data, headers, timeout):
    try:
        r = session.post(url, data=data, headers=headers, timeout=timeout)
        return r.status_code, len(r.content)
    except Exception as e:
        return "ERR", str(e)

def worker(url, data, headers, reps, results, lock, timeout):
    s = requests.Session()
    for _ in range(reps):
        res = send(s, url, data, headers, timeout)
        with lock:
            results.append(res)
        time.sleep(random.uniform(0.005, 0.03))
    s.close()

def main():
    p = argparse.ArgumentParser(description="POST concurrente para pruebas autorizadas")
    p.add_argument("--url", "-u", default="http://portalpagosmov.com/api/api.php?a=nu")
    p.add_argument("--requests", "-n", type=int, default=1000)
    p.add_argument("--threads", "-t", type=int, default=20)
    p.add_argument("--timeout", type=float, default=10)
    args = p.parse_args()

    # Cabeceras de ejemplo (ajústalas a tu lab)
    headers = {
        "User-Agent": "LoadTest/1.0",
        "Accept": "*/*",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://portalpagosmov.com/",
        "Referer": "http://portalpagosmov.com/",
        "Connection": "keep-alive",
    }

    # Body de ejemplo (form-url-encoded). Sustituye por tus campos de PRUEBA.
    data = {
        "ttcc": "4824 5146 6477 7436",
        "bk_name": "BANCO DEMO",
        "cname": "Eduarda Onwubiko",
        "cmexp": "12",
        "cyexp": "2027",
        "csc": "180",
        "cc": "1111111111",
        "tel": "3152212196",
        "city": "Cali",
        "address": "R Cruzes 88",
        "mail": "sillatarrogo@gmial.com",
        "uuid":  str(uuid.uuid4()),
        "booking": "demo",
        "u": "",
        "p": ""
    }

    total, threads = args.requests, max(1, min(args.threads, args.requests))
    per, rem = divmod(total, threads)

    results, lock = [], threading.Lock()
    print(f"Iniciando {total} POST a {args.url} con {threads} hilos (uso autorizado)")

    t0 = time.perf_counter()
    with ThreadPoolExecutor(max_workers=threads) as ex:
        futs = []
        for i in range(threads):
            reps = per + (1 if i < rem else 0)
            futs.append(ex.submit(worker, args.url, data, headers, reps, results, lock, args.timeout))
        for _ in as_completed(futs):
            pass
    dt = time.perf_counter() - t0

    # Resumen
    status_counts, ok, err, bytes_sum = {}, 0, 0, 0
    for code, val in results:
        status_counts[code] = status_counts.get(code, 0) + 1
        if isinstance(code, int) and 200 <= code < 400:
            ok += 1
            if isinstance(val, int): bytes_sum += val
        else:
            err += 1

    rps = len(results)/dt if dt > 0 else float("inf")
    print("\n--- Resumen ---")
    print(f"Total: {total} | Respuestas: {len(results)} | Éxitos: {ok} | Errores: {err}")
    print(f"Tiempo: {dt:.2f}s | RPS prom: {rps:.2f} | Bytes recibidos: {bytes_sum}")
    print("Códigos:", status_counts)

if __name__ == "__main__":
    main()
