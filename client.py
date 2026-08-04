import socket

HOST = "127.0.0.1"
PORT = 5310

trama = (
    "STT;1700020206;3FFFFF;170;1.0.17;1;"
    "20260728;14:30:00;095949C8;732;101;"
    "6981;25;+3.527648;-76.613550;0.00;0.00;"
    "14;1;00000000;00000000;0;1;5591"
)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(trama.encode("utf-8"))

print("Trama enviada correctamente")