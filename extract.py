import json
import time
from pathlib import Path

import requests

list_url = "https://pokeapi.co/api/v2/pokemon?limit=2000"

response = requests.get(list_url)
response.raise_for_status()
pokemon_list = response.json()["results"]

print(f"Found {len(pokemon_list)} Pokemon")

output_dir = Path("data/raw/pokemon")
output_dir.mkdir(parents=True, exist_ok=True)

for pokemon in pokemon_list:
    output_file = output_dir / f"{pokemon['name']}.json"

    if output_file.exists():
        continue

    response = requests.get(pokemon["url"])
    response.raise_for_status()

    output_file.write_text(json.dumps(response.json(), indent=2))
    print(f"Saved {pokemon['name']}")

    time.sleep(0.1)

print("Done")