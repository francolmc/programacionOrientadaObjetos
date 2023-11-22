import requests
import json
from user import User

# URL de la API
url = "https://jsonplaceholder.typicode.com/users/4"

response = requests.get(url)

if response.status_code == 200:
    json_data = response.text
    diccionario = json.loads(json_data)
    user = User()
    user.set_from_json(diccionario)
    print(user)
else:
    print(f"Hubo un error con la peticion con error: {response.status_code}")