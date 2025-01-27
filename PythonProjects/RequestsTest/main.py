import requests

URL = 'https://api.pokemonbattle.ru/v2'
Token = '1'
Header = {'Content-Type' : 'application/json', 'trainer_token' : Token}

Body_create = {
    "name": "generate",
    "photo_id": -1
}

Body_put = {
    "pokemon_id": "204968",
    "name": "Чермандер",
    "photo_id": 2
}

Body_pokeball = {
    "pokemon_id": "204968"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = Header, json = Body_create)
print(response_create.text)

response_put = requests.put(url = f'{URL}/pokemons', headers = Header, json = Body_put)
print(response_put.text)

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = Header, json = Body_pokeball)
print(response_pokeball.text)