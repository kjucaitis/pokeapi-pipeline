import json
from pathlib import Path

import requests

url = "https://pokeapi.co/api/v2/pokemon/bulbasaur"

response = requests.get(url)
response.raise_for_status()
data = response.json()

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / f"{data['name']}.json"
output_file.write_text(json.dumps(data, indent=2))

print(f"Saved {output_file}")