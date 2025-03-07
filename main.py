import funciones
from fastapi import FastAPI

app = FastAPI()

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
        summary="Nutrición: 5.- Sustituir alimento ")
async def sustituir_alimento(prompt: str):
    return funciones.getSustitucion(prompt)