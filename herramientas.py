import os
import socket
from openai import OpenAI

def obtenClienteOpenAI():
    if local_check():
        print("Estoy en LOCAL...")
        import bridges
        buzz = bridges.buzz
        llave = bridges.llave
    else:
        print("Estoy en REMOTO...")
        buzz = os.getenv("buzz")
        llave = os.getenv("llave")

    client = OpenAI(api_key=buzz)
    return client

def local_check(): 

    hostname = socket.gethostname()

    if hostname == 'nombre_del_servidor':
        print("Ejecutando en el servidor")
        return False
    else:
        print("Ejecutando en local")
        return True