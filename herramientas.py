import os
import socket
from openai import OpenAI
import time

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
    #r-moibe-nowme
    print("Dentro de local_check... , el hostname es: ", hostname)

    if "r-moibe-nowme" in hostname:
        print("Ejecutando en el servidor")
        return False
    else:
        print("Ejecutando en local")
        return True