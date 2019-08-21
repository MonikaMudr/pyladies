import requests

with open('token.txt') as f:
    token = f.read()

headers = {'Authorization': 'token ' + token}

url = 'https://api.github.com/user/starred/pyvec/naucse.python.cz'
page = requests.put(url, headers=headers)

page.raise_for_status()