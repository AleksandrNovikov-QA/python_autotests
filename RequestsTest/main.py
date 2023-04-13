import requests
token = '0def22a3fc99f6445c817f5eb3aba983'
base_url = 'https://pokemonbattle.me:9104/'

#создание покемона POST
response_add_pokemon = requests.post(f'{base_url}pokemons', headers={'trainer_token' : token}, json={
    "name": "Мегазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})

print(response_add_pokemon.text)

#смена имени покемона PUT
change_name_pokemon = requests.put(f'{base_url}pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": "9152",
    "name": "Мега",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}) 

print(change_name_pokemon.text)

#Поймать покемона в покеболл POST
add_pokemon_in_pokeball = requests.post(f'{base_url}trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": "9154"
}) 

print(add_pokemon_in_pokeball.text)