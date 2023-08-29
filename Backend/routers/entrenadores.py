from fastapi import APIRouter
import mysql.connector
from pydantic import BaseModel

# conexion con la base de datos
conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="revi123",
    database="entrenadores_pokemon"
)

router = APIRouter()

#  modelo de datos
class entrenadores(BaseModel):
    Pokemon: str
    Entrenador: str    


# Ruta para obtener todos los entrenadores
@router.get("/entrenadores")
async def get_entrenadores():
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM entrenadores")
    columns = cursor.column_names
    entrenadores = []
    for row in cursor.fetchall():
        entrenador = dict(zip(columns, row))
        entrenadores.append(entrenador)
    cursor.close()
    return entrenadores


# Ruta para actualizar un entrenador por su nombre
@router.put("/entrenadores/{nombreEntrenador}")
async def update_entrenador(nombreEntrenador: str,updated_entrenador: entrenadores):
    cursor = conexion.cursor()
    cursor.execute("UPDATE entrenadores SET Pokemon = %s WHERE Entrenador = %s",
                   (updated_entrenador.Pokemon, nombreEntrenador))
    conexion.commit()
    cursor.close()
    return updated_entrenador


# Ruta para crear un entrenador
@router.post("/nuevoentrenador")
async def create_entrenador(entrenador: entrenadores):
    cursor = conexion.cursor()
    cursor.execute("INSERT INTO entrenadores (Pokemon, Entrenador) VALUES (%s, %s)",
                   (entrenador.Pokemon, entrenador.Entrenador))
    conexion.commit()
    cursor.close()
    return entrenador

# Ruta para eliminar una entrenadores
@router.delete("/entrenadores/{nombreEntrenador}")
async def delete_subsidiaria(nombreEntrenador: str):
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM entrenadores WHERE Entrenador = %s", (nombreEntrenador,))
    conexion.commit()
    cursor.close()
    return {"message": "Entrenador eliminado"}

