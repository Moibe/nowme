import asistente
import operacionesIA


def getMacronutrientes(prompt):
    return operacionesIA.consulta(asistente.macronutrientes, prompt)

def getComidas(prompt):
    return operacionesIA.consulta(asistente.comidas, prompt)

def getAlimentos(prompt):
    return operacionesIA.consulta(asistente.alimentos, prompt)

def getReceta(prompt):
    return operacionesIA.consulta(asistente.receta, prompt)

def getSustitucion(prompt):
    return operacionesIA.consulta(asistente.sustitucion, prompt)
