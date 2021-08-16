import requests

url = "https://jsonplaceholder.typicode.com/users"

r = requests.get(url)

data = r.json()

for record in data:
    print(record["name"]+","+record["username"]+","+record["company"]["name"])