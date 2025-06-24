# Laboratorio: Ransomware en Cadena de Suministro (Simulación IFX Networks)
=====================================

## 🧠 Descripción del escenario

El 12 de septiembre de 2023, IFX Networks—proveedor MSP de servicios en la nube y telecomunicaciones presente en 17 países de Latinoamérica—fue víctima de un ataque de ransomware que comprometió algunas de sus máquinas virtuales.

El alcance del ataque fue significativo: más de 760 entidades públicas y privadas en Colombia, Chile y Panamá resultaron afectadas. En Colombia, se reportaron impactos en al menos 46 portales e infraestructuras críticas, incluidos sitios de la rama judicial, el Ministerio de Salud y varias superintendencias.

La autoría fue atribuida al grupo de ransomware RansomHouse. En las máquinas de IFX apareció un mensaje de los atacantes, firmado como “Bienvenido a Ransomhouse”, en el que se confirmaba el cifrado de la infraestructura y se anunciaba la filtración de datos y la destrucción de respaldos, exigiendo contacto para negociar el rescate.


## ⚙️ Componentes


1. IFX Server (ifx-server)

  + Contenedor con Apache HTTPD que expone un archivo patch.sh.

  + Este parche es un script malicioso que cifra archivos .txt en los clientes.

2. Clientes afectados

+  Se crean 3 clientes simulando instituciones:

  + cliente-salud

  + cliente-judicial

  + cliente-sic

Cada uno crea dos archivos .txt simulando documentos internos.

Descargan y ejecutan automáticamente el parche desde el servidor.

## 🎯 ¿Cómo funciona?


1. Clona o descarga este repositorio en tu máquina local. :

```bash
   git clone https://github.com/tu-usuario/ransonware-lab.git
   cd ransonware-lab/
```

2. Inicio del laboratorio Ejecuta:

```bash
docker-compose up --build
```

3. Ejecución de la simulación

+ ifx-server inicia Apache y pone a disposición patch.sh.

+ Los clientes arrancan, crean /data/doc1.txt y /data/doc2.txt, y luego:

    - Esperan 5 segundos.

    - Usan curl para descargar http://ifx-server/patch.sh.

    - Lo ejecutan, lo cual:

        - Cifra los .txt con OpenSSL.

        - Borra los originales.

        - Muestra los archivos .enc resultantes.


4 Resultado esperado En la consola de cada cliente verás :

+ Contenido en /data después del parche:

```bash
-rw-r--r--    1 root     root        32 doc1.txt.enc
-rw-r--r--    1 root     root        48 doc2.txt.enc
```

## 🧪¿Dónde están los archivos?

Los archivos existen dentro del contenedor, no en el host.

Para verlos manualmente:

```bash
─$ docker exec -it cliente-salud sh
/data # ls
doc1.txt.enc  doc2.txt.enc
/data # cat doc1.txt.enc
Salted__�:3�\Fv�4bus��A-�����3/data #
```


🛡️ Advertencia
Este laboratorio simula técnicas utilizadas por actores maliciosos. Está destinado exclusivamente para entornos de laboratorio, propósitos académicos o pruebas de concienciación. No lo utilices en redes de producción ni contra usuarios reales.
