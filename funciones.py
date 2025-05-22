import asistentes
import operacionesIA

asistente_actual = "produccion"

#Nutrición 

def getMacronutrientes(prompt):
    return operacionesIA.consulta(asistentes.asistente["macronutrientes"], prompt)

def getComidas(prompt):
    return operacionesIA.consulta(asistentes.asistente["comidas"], prompt)

def getAlimentos(prompt):
    return operacionesIA.consulta(asistentes.asistente["alimentos"], prompt)

def getReceta(prompt):
    return operacionesIA.consulta(asistentes.asistente["receta"], prompt)

def getSustitucion(prompt):
    return operacionesIA.consulta(asistentes.asistente["sustitucion"], prompt)

#Entrenamiento

def getDistribucionGruposMusculares(prompt):
    return operacionesIA.consulta(asistentes.grupos_musculares, prompt)

def getEjercicios(prompt):
    return operacionesIA.consulta(asistentes.eleccion_ejercicios, prompt)

def getBloques(prompt):
    return operacionesIA.consulta(asistentes.distribucion_bloques, prompt)

def getCircuito(prompt):
    return operacionesIA.consulta(asistentes.distribucion_circuito, prompt)

def getSumatoria(prompt):
    return operacionesIA.consulta(asistentes.distribucion_sumatoria, prompt)

def getCardio(prompt):
    return operacionesIA.consulta(asistentes.distribucion_sumatoria, prompt)