import socket

import psycopg

from database import guardar_posicion
from parser import parse_stt


HOST = "0.0.0.0"
PORT = 5310
BUFFER_SIZE = 4096


def mostrar_datos(datos: dict) -> None:
    print("\n========== GPS ==========")

    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

    print("=========================\n")


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen()

    print(f"Servidor TCP escuchando en el puerto {PORT}...")

    while True:
        connection, address = server.accept()

        print(f"\nCliente conectado desde {address}")

        with connection:
            while True:
                data = connection.recv(BUFFER_SIZE)

                if not data:
                    print(f"Cliente desconectado: {address}")
                    break

                trama = data.decode(
                    "utf-8",
                    errors="replace",
                ).strip()

                print(f"Trama original: {trama}")

                try:
                    datos = parse_stt(trama)
                    guardar_posicion(datos, trama)

                    mostrar_datos(datos)
                    print("Posición guardada correctamente en PostgreSQL")

                except ValueError as error:
                    print(f"Trama rechazada: {error}")

                except psycopg.Error as error:
                    print(f"Error al guardar en PostgreSQL: {error}")

                except Exception as error:
                    print(f"Error inesperado: {error}")