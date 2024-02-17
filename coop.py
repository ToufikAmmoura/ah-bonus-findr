import requests

def main():
  url = 'https://api.microservice.coop.nl/offers/?formula=FULL'
  response = requests.get(url)
  json_response = response.json()

  products = []
  for element in json_response:
    product = {}

    product['name'] = element['name']
    product['promotion'] = element['sticker']
    product['old price'] = element['formulaInformations'][0]['originalPrice']
    product['new price'] = element['formulaInformations'][0]['newPrice']

    products.append(product)

  return products
