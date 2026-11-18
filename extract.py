import requests

url = "https://pokeapi.co/api/v2/pokemon/bulbasaur"

response = requests.get(url)
response.raise_for_status()

data = response.json()
print(data["name"], data["id"])
print(data.keys())