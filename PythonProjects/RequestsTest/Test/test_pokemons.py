import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
Token = '1'
Header = {'Content-Type' : 'application/json', 'trainer_token' : Token}
trainer_id = '21957'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_kveri_id():
    response_kveri = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : trainer_id} )
    assert response_kveri.json()["data"][0]["trainer_name"] == "Рагнар"