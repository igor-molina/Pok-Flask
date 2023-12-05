from flask import jsonify, current_app
from app import app
import requests

@app.route('/get_pokemon/<pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    api_url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}/'
    
    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            pokemon_data = response.json()
            formatted_data = format_pokemon_data(pokemon_data)
            return jsonify(formatted_data)
        else:
            return jsonify({'error': f'Erro na API: {response.status_code}'})

    except Exception as e:
        return jsonify({'error': f'Erro na solicitação: {str(e)}'})
    
def format_pokemon_data(pokemon_data):
    formatted_data = {
        'name': pokemon_data['name'],
        'id': pokemon_data['id'],
        'types': [type_info['type']['name'] for type_info in pokemon_data['types']],
        'abilities': [ability_info['ability']['name'] for ability_info in pokemon_data['abilities']],
        'sprite': pokemon_data['sprites']['front_default'],
    }
    return formatted_data

@app.route('/get_all_pokemons/<endpoint>', methods=['GET'])
def get_all_pokemons(endpoint):
    api_url = f'https://pokeapi.co/api/v2/{endpoint}/'

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            pokemon_data = response.json()
            return jsonify(pokemon_data)
        else:
            return jsonify({'error': f'Erro na API: {response.status_code}'})
    except Exception as e:
        return jsonify({'error': f'Erro na solicitação: {str(e)}'})