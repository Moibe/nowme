import funciones
from fastapi import FastAPI

app = FastAPI()

#NUTRICIÓN

#1.- Obtener distribución macronutrientes.
@app.post(
        "/macronutrientes/",
        tags=["Nutrición"],
        summary="1.- Obtener Distribución de Macronutrientes")
async def macronutrientes(prompt: str):
    return funciones.getMacronutrientes(prompt)
    
#2.- Obtener distribución comidas.
@app.post(
        "/comidas/",
        tags=["Nutrición"],
        summary="2.- Obtener Distribución de Comidas Durante el Día")
async def comidas(prompt: str):
    return funciones.getComidas(prompt)

#3.- Obtener lista alimentos.
@app.post(
        "/lista_alimentos/",
        tags=["Nutrición"],
        summary="Nutrición: 3.- Obtener Alimentos para una Comida")
async def lista_alimentos(prompt: str):
    return funciones.getAlimentos(prompt)

#4.- Obtener receta.
@app.post(
        "/receta/",
        tags=["Nutrición"],
        summary="Nutrición: 4.- Generar Receta para una Comida")
async def receta(prompt: str):
    return funciones.getReceta(prompt)

#5.- Sustituir alimento.
@app.post(
        "/sustituir_alimento/",
        tags=["Nutrición"],
        summary="Nutrición: 5.- Sustituir Alimento ")
async def sustituir_alimento(prompt: str):
    return funciones.getSustitucion(prompt)

#ENTRENAMIENTO

#1.- Obtener distribución de grupos musculares.
@app.post(
        "/distribucion_musculos/",
        tags=["Entrenamiento"],
        summary="1.- Obtener Distribución de Grupos Musculares")
async def macronutrientes(prompt: str):
    return funciones.getDistribucionGruposMusculares(prompt)

#2.- Obtener ejercicios.
@app.post(
        "/ejercicios/",
        tags=["Entrenamiento"],
        summary="2.- Obtener Selección de Ejercicios")
async def macronutrientes(prompt: str):
    return funciones.getEjercicios(prompt)

#3.- Obtener distribución por bloques.
@app.post(
        "/bloques/",
        tags=["Entrenamiento"],
        summary="3A.- Obtener Distribución de Bloques")
async def macronutrientes(prompt: str):
    return funciones.getBloques(prompt)

#4.- Obtener distribución en circuito.
@app.post(
        "/circuito/",
        tags=["Entrenamiento"],
        summary="3B.- Obtener Distribución en Circuito")
async def macronutrientes(prompt: str):
    return funciones.getCircuito(prompt)

#5.- Obtener distribución en sumatoria.
@app.post(
        "/sumatoria/",
        tags=["Entrenamiento"],
        summary="3C.- Obtener Distribución en Sumatoria")
async def macronutrientes(prompt: str):
    return funciones.getSumatoria(prompt)

#6.- Obtener distribución de cardio.
@app.post(
        "/cardio/",
        tags=["Entrenamiento"],
        summary="4.- Obtener Distribución en Cardio")
async def macronutrientes(prompt: str):
    return funciones.getSumatoria(prompt)