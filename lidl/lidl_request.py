import requests
from lxml import html

response = requests.get('https://www.lidl.nl/c/aanbiedingen/a10008785')

tree = html.fromstring(response.content)
elements = tree.xpath('//div[contains(@fulltitle, "")]/@fulltitle')

for el in elements:
  print(el)

