import requests
import json


with open('token.txt') as f:
    token = f.read()

headers = {'Authorization': 'token ' + token}

page = requests.get('https://api.github.com/emojis', headers=headers)
page.raise_for_status()

data = json.loads(page.text)

print(json.dumps(data, ensure_ascii=True, indent=2))

print(data['100'])

