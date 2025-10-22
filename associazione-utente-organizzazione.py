import requests

api_key = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJORjdFMWctX2dFSmhqZ1U3TkJOSThnV1V0SUZFa2I5MnNzNEVQT3lpeVVjIiwiaWF0IjoxNzYwMDE5MjI2fQ.VdeEqFXTW8DSzLYCa58m7BNTfLUxHGH_rtSgvDQqmYQ'
base_url = 'https://localhost:8443/catalog'

endpoint = f'{base_url}/api/3/action/member_create'
headers = {'Authorization': api_key}

data = {
    'id': 'members',         # nome o ID dell'organizzazione
    'object': 'tobia',       # username dell'utente
    'object_type': 'user',
    'capacity': 'member'     # oppure 'editor', 'admin'
}

response = requests.post(endpoint, json=data, headers=headers)
print(response.json())