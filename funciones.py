import asistente
import operacionesIA

#Nutrición 

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

#Entrenamiento

def getDistribucionGruposMusculares(prompt):
    return operacionesIA.consulta(asistente.grupos_musculares, prompt)

def getEjercicios(prompt):
    return operacionesIA.consulta(asistente.eleccion_ejercicios, prompt)

def getBloques(prompt):
    return operacionesIA.consulta(asistente.distribucion_bloques, prompt)

def getCircuito(prompt):
    return operacionesIA.consulta(asistente.distribucion_circuito, prompt)

def getSumatoria(prompt):
    return operacionesIA.consulta(asistente.distribucion_sumatoria, prompt)

def getCardio(prompt):
    return operacionesIA.consulta(asistente.distribucion_sumatoria, prompt)