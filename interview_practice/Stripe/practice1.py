import requests
import pprint

r = requests.get("https://cat-fact.herokuapp.com/facts")
results = r.json()

print(results.all)

