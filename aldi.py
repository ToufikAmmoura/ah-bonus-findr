import asyncio
import aiohttp
import requests
from lxml import html

# https://www.aldi.nl/content/aldi/netherlands/nl/web-consumer/aanbiedingen/wk07_vanaf_maandag12-02/jcr:content/par/article_section/par/tiles2_1134132180/par/articletile20.html


def get_article_urls():
  response = requests.get('https://www.aldi.nl/aanbiedingen.html')
  tree = html.fromstring(response.content)
  url_paths = tree.xpath('//div[contains(@data-tile-url, "") and contains(@class, "article")]/@data-tile-url')

  product_urls = []

  for path in url_paths:
    base_url = 'https://www.aldi.nl'
    product_url = base_url + path
    product_urls.append(product_url)

  return product_urls

async def fetch_url(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      return await response.text()
    
async def fetch_all_product_data(product_urls):
  tasks = [fetch_url(url) for url in product_urls]
  results = await asyncio.gather(*tasks)
  return results

def extract_text(tree, xpath):
  try:
    return tree.xpath(xpath)[0].text.strip()
  except IndexError:
    return None

def get_title(tree):
  title_xpath = '//span[@class="mod-article-tile__title"]'
  return extract_text(tree, title_xpath)

def get_promotion(tree):
  promotion_xpath = '//span[contains(@class, "price__previous-percentage")]/span'
  return extract_text(tree, promotion_xpath)

def get_prices(tree):
  old_price_xpath = '//s[@class="price__previous"]'
  new_price_xpath = '//span[@class="price__wrapper"]'

  old_price = extract_text(tree, old_price_xpath)
  new_price = extract_text(tree, new_price_xpath)

  return old_price, new_price

def main():
  product_urls = get_article_urls()
  product_data = asyncio.run(fetch_all_product_data(product_urls))

  products = []

  for data in product_data:
    product = {}

    tree = html.fromstring(data)

    product['title'] = get_title(tree)
    product['promotion'] = get_promotion(tree)
    product['old price'], product['new price'] = get_prices(tree)

    products.append(product)

  return products