import json
from pathlib import Path

import requests

list_url = "https://pokeapi.co/api/v2/pokemon?limit=2000"

response = requests.get(list_url)
response.raise_for_status()
pokemon_list = response.json()["results"]

print(f"Found {len(pokemon_list)} Pokemon")
print(pokemon_list[:3])

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "pokemon_list.json"
output_file.write_text(json.dumps(pokemon_list, indent=2))

print(f"Saved {output_file}")