import requests
from lxml import html
import json

def main():
  response = requests.get('https://www.lidl.nl/c/aanbiedingen/a10008785')
  tree = html.fromstring(response.content)
  product_records = tree.xpath('//div[@data-selector="PRODUCT"]/div/@data-grid-data') 
  
  products = []

  for record in product_records:
    product = {}

    parsed_record = json.loads(record)

    # title
    product['title'] = parsed_record[0]['fullTitle']

    # promotion
    product['promotion'] = parsed_record[0]['price']['discount']['discountText']
    
    # old price (it's zero if old price is not displayed)
    old_price = parsed_record[0]['price']['oldPrice']
    product['old price'] = old_price if old_price != 0 else None
    
    # new price
    product['new price'] = parsed_record[0]['price']['price']

    products.append(product)

  return products