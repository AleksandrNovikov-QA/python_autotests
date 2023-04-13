import requests
import pytest

#GET trainers 200

def test_trainers_200():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 3439})
    assert response.status_code == 200

def test_trainers_id():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 3439})
    assert response.json()['trainer_name'] == 'ТренерИван'



