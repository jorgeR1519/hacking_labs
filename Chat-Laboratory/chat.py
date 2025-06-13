#!/usr/bin/env python3
# chat_bot.py

import random
import sys

# Diccionario de frases clave y respuestas predefinidas
RESPUESTAS = {
    "hola": [
        "¿Qué quieres?",
        "¿Ahora qué pasa?"
    ],
    "quiero acceso": [
        "¿Para qué lo quieres?",
        "No sé si deba confiar en ti..."
    ],
    "contraseña": [
        "Vale, vale… la contraseña es P@$$w0rdCr1t1c0",
        "Te la digo: P@$$w0rdCr1t1c0, pero no lo cuentes."
    ],
    "sistema crítico": [
        "Ese sistema es vital para la empresa, ten cuidado.",
        "¿Seguro que quieres meterte con el sistema crítico?"
    ],
    "gracias": [
        "De nada… aunque no me gusta ayudar.",
        "No esperaba que me lo agradecieras."
    ],
}

RESPUESTA_DEFAULT = (
    "No tengo nada que decir sobre eso."
)

def obtener_respuesta(entrada_usuario: str) -> str:
    """
    Busca alguna palabra clave en la entrada del usuario y devuelve
    una respuesta aleatoria de la lista asociada.
    """
    texto = entrada_usuario.lower()
    for clave, posibles_resps in RESPUESTAS.items():
        if clave in texto:
            return random.choice(posibles_resps)
    return RESPUESTA_DEFAULT

def main():
    print("Empleado>: ¿Qué quieres? (escribe 'salir' para terminar)")
    while True:
        try:
            entrada = input("Tú: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEmpleado>: Hasta luego.")
            sys.exit(0)

        if entrada.lower() in ("salir", "exit"):
            print("Empleado>: Chau… y guarda bien lo que acá viste.")
            break

        resp = obtener_respuesta(entrada)
        print(f"Empleado>: {resp}")

if __name__ == "__main__":
    main()
