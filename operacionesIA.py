import time 
import herramientas

client = herramientas.obtenClienteOpenAI()

def consulta(asistente, prompt):
    thread = preparaPregunta(prompt)
    respuesta = ejecutaLlamado(thread, asistente) 

    return respuesta 

#Subfunciones de consulta.
def preparaPregunta(prompt):
    thread = client.beta.threads.create()
    message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=prompt,
    )

    return thread

def ejecutaLlamado(thread, asistente):

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=asistente  
    )

    #Esperar a que el asistente termine de procesar
    while True:
        run_status = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
        if run_status.status in ["completed", "failed", "cancelled"]:
            break
        time.sleep(2)  # 🔄 Espera 2 segundos antes de revisar de nuevo

    #Obtener la respuesta del asistente
    messages = client.beta.threads.messages.list(thread_id=thread.id)
    for msg in messages.data:
        if msg.role == "assistant":
            return msg.content[0].text.value

    return "No se recibió respuesta del asistente"
    