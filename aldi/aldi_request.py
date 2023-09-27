import requests
from lxml import html

response = requests.get('https://www.aldi.nl/aanbiedingen.html')

with open('aldi.html', 'w') as file:
  file.write(response.text)

tree = html.fromstring(response.content)
elements = tree.xpath('//div[contains(@data-tile-url, "") and contains(@class, "article")]/@data-tile-url')

article_titles = []

for el in elements:
  base_url = 'https://www.aldi.nl'
  article_url = base_url + el
  article_response = requests.get(article_url)
  tree = html.fromstring(article_response.content)
  article_title = tree.xpath('//span[@class="mod-article-tile__title"]')[0]
  article_titles.append(article_title.text.strip())

for article_title in article_titles:
  print(article_title)


# mogelijke xpath: //div[contains(@data-tile-url, "") and contains(@class, "article")]/@data-tile-url
# xpath titel: //span[@class="mod-article-tile__title"]