import asyncio
import aiohttp
import requests
from lxml import html

response = requests.get('https://www.aldi.nl/aanbiedingen.html')

tree = html.fromstring(response.content)
elements = tree.xpath('//div[contains(@data-tile-url, "") and contains(@class, "article")]/@data-tile-url')

article_urls = []
results = []
article_titles = []

for el in elements:
  base_url = 'https://www.aldi.nl'
  article_url = base_url + el
  article_urls.append(article_url)

async def fetch_url(url):
  async with aiohttp.ClientSession() as session:
    async with session.get(url) as response:
      return await response.text()
    
async def main():
  tasks = [fetch_url(url) for url in article_urls]
  results = await asyncio.gather(*tasks)
  return results

if __name__ == '__main__':
  results = asyncio.run(main())

  for result in results:
    tree = html.fromstring(result)
    article_title = tree.xpath('//span[@class="mod-article-tile__title"]')[0]
    article_titles.append(article_title.text.strip())    
    print(article_title.text.strip())
