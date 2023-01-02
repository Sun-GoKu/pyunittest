import requests

resp = requests.get('http://127.0.0.1')
# r = resp.json()
print(resp.status_code)