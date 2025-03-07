import os
import socket
from openai import OpenAI
import time

def obtenClienteOpenAI():
    if local_check():
        print("Estoy en LOCAL...")
        time.sleep(18)
        import bridges
        buzz = bridges.buzz
        llave = bridges.llave
    else:
        print("Estoy en REMOTO...")
        time.sleep(18)
        buzz = os.getenv("buzz")
        llave = os.getenv("llave")

    client = OpenAI(api_key=buzz)
    return client

def local_check(): 

    hostname = socket.gethostname()
    print("Dentro de local_check... , el hostname es: ", hostname)
    time.sleep(18)

    if hostname == 'nombre_del_servidor':
        print("Ejecutando en el servidor")
        return False
    else:
        print("Ejecutando en local")
        return True