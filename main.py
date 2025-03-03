from fastapi import FastAPI
import IA

app = FastAPI()

#1.- Obtener distribución macronutrientes.
@app.post("/macronutrientes/")
async def macronutrientes(prompt: str):
    return IA.getMacronutrientes(prompt)
    
#2.- Obtener distribución comidas.
@app.post("/comidas/")
async def comidas(prompt: str):
    return IA.getComidas(prompt)

#3.- Obtener lista alimentos.
@app.post("/lista_alimentos/")
async def lista_alimentos(prompt: str):
    return IA.getAlimentos(prompt)

#4.- Obtener receta.
@app.post("/receta/")
async def receta(prompt: str):
    return IA.getReceta(prompt)

#5.- Sustituir alimento.
@app.post("/sustituir_alimento/")
async def sustituir_alimento(prompt: str):
    return IA.getSustitucion(prompt)