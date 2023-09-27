import requests

response = requests.get('https://api.microservice.coop.nl/offers/?formula=FULL&_date=2023-09-27')
data = response.json()

print(len(data))
for article in data:
  print(article['name'])
