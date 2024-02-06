import requests
from datetime import datetime, timedelta

def get_monday_date():
  today = datetime.now()
  monday = today - timedelta(days=today.weekday())
  return monday.strftime("%Y-%m-%d")


url = 'https://api.microservice.coop.nl/offers/?formula=FULL&_date=' + get_monday_date()
response = requests.get(url)
data = response.json()

for article in data:
  print(article['name'])
