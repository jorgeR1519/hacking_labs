#!/bin/sh
echo "[*] Procesando archivo subido..."

# Aquí simulamos que Ghostscript genera una miniatura (como si fuera un servidor real)
gs -dBATCH -dNOPAUSE -sDEVICE=png16m -sOutputFile=thumb.png fake.pdf

echo "[*] Listo."
