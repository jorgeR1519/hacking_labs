#!/bin/bash
echo "Content-type: text/plain"
echo ""
# Aquí está el fallo clásico Shellshock:
echo "User-Agent is: $HTTP_USER_AGENT"
bash -c "echo Exploit ejecutado; id"

