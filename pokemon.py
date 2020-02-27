import requests
import json
import matplotlib.pyplot as plt
poke_url = 'https://pokeapi.co/api/v2/pokemon/?limit=1000'

poke_json = requests.get(poke_url).text
pokemon = json.loads(poke_json)
id_list = []
weight_list = []
for result in pokemon['results']:
    res_json = requests.get(result['url']).json()
    id_list.append(res_json['id'])
    weight_list.append(res_json['weight'])

plt.plot(id_list, weight_list)
plt.show()

print(result['name'], "Weight", res_json['weight'])
