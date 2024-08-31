import requests
url=('https://random-data-api.com/api/v2/users')
data =requests.get(url)
print(data.json())