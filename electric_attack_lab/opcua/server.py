import asyncio
from asyncua import Server, ua

async def main():
    server = Server()
    # Endpoint
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # Permitir tráfico no cifrado y anónimo
    server.set_security_policy([ua.SecurityPolicyType.NoSecurity])
    server.set_security_IDs(["Anonymous"])  # habilita al usuario 'Anonymous'

    # Inicia el servidor YA configurado
    await server.init()
    await server.start()

    # Ahora registra el namespace y la variable
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    var = await server.nodes.objects.add_variable(idx, "Voltage", 400.0)
    await var.set_writable()  # ahora funciona sin permisos extra

    print("OPC UA corriendo en 4840")
    try:
        while True:
            await asyncio.sleep(1)
    finally:
        await server.stop()

if __name__ == "__main__":
    asyncio.run(main())

