import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '78a9035808396e789b1b51407be8d998'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_newpokemon = {
    "name": "Бульбазавр",
    "photo_id": 1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_newpokemon)
print(response_create.text)

pokemon_id = response_create.json()['id']

body_newname = {
    "pokemon_id": pokemon_id,
    "name": "Jackson",
    "photo_id": 1
}

body_pokeball = {
    "pokemon_id": pokemon_id
}

response_newname = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_newname)
print(response_newname.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response_pokeball.text)