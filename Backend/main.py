from routers import pokemons, entrenadores
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# inicializar servidor uvicorn main:app --reload
app.include_router(pokemons.router)
app.include_router(entrenadores.router)

if __name__ == "__main__":
   import uvicorn
   uvicorn.run(app, host="127.0.0.1", port=8000)