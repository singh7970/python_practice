import requests
responce=requests.get('https://random-data-api.com/api/v2/users')
print(responce.json())