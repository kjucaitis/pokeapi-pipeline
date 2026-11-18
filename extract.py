import json
import time
from pathlib import Path

import requests


def get_json(url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            print(f"Attempt {attempt} failed for {url}: {error}")
            if attempt == retries:
                raise
            time.sleep(5)


list_url = "https://pokeapi.co/api/v2/pokemon?limit=2000"
pokemon_list = get_json(list_url)["results"]

print(f"Found {len(pokemon_list)} Pokemon")

output_dir = Path("data/raw/pokemon")
output_dir.mkdir(parents=True, exist_ok=True)

for pokemon in pokemon_list:
    output_file = output_dir / f"{pokemon['name']}.json"

    if output_file.exists():
        continue

    data = get_json(pokemon["url"])
    output_file.write_text(json.dumps(data, indent=2))
    print(f"Saved {pokemon['name']}")

    time.sleep(0.1)

print("Done")