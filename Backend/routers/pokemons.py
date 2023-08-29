from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

pokeapi_base_url = "https://pokeapi.co/api/v2"

@router.get("/pokemon/{pokemon_name}")
async def get_pokemon_info(pokemon_name: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{pokeapi_base_url}/pokemon/{pokemon_name}")
        if response.status_code != 200:
            raise HTTPException(status_code=404, detail="Pokémon not found")
        data = response.json()

    pokemon_info = {
        "name": data["name"],
        "image": data["sprites"]["front_default"],
        "types": [type_info["type"]["name"] for type_info in data["types"]]
    }
    return pokemon_info
