import requests

# URL de la API
url = "https://rickandmortyapi.com/api/character/1"

response = requests.get(url)

if response.status_code == 200:
    json_data = response.json();
    print(json_data)
else:
    print(f"Hubo un error con la peticion con error: {response.status_code}")