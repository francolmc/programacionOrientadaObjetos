import requests

def obtener_personaje_api_por_id(id):
    # Utiliza la API de Rick and Morty para obtener información sobre personajes en formato JSON
    url = f"https://rickandmortyapi.com/api/character/{id}"
    response = requests.get(url)
    personaje_json = response.json()
    return personaje_json