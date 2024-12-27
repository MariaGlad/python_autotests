import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '78a9035808396e789b1b51407be8d998'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '12906'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers')
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers?trainer_id=12906')
    assert response_get.json()["data"][0]["trainer_name"] == 'Maria1'