# discount-scraper
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Simple scripts that scrape some supermarket sites to see what products are in a discount at the moment. It grabs the titles, old prices and new prices of the products with a discount. Not a lot of functionality, it's mainly a project to figure out what techniques the different sites use with some simple reverse engineering for fun.


## Requirements

- Python3
- Chrome Webdriver

## Usage

```python
python3 discounts.py
```

## How it works

### Albert Heijn
In the past I could access their API through a GraphQL request but they disabled that option. So now I use `selenium`, grab the product cards and extract the needed attributes out of them.

### Jumbo
Similar `selenium` solution as Albert Heijn.

### Aldi
Aldi is a fun one. We use a simple `GET` request to get the discount page, this doesn't contain anything except a bunch of url-paths to the products in a discount. Performing a GET request with `aldi.nl` as base-url and adding the url-path will retrieve a site with the attributes of the discounted product. Here we extract the needed elements with `lxml`.

The fun part is that since we're performing so many `GET` request it's way too slow doing them one by one. So parallelization came to the rescue. Using `asyncio` and `aiohttp` I get the product attributes of more than 100 products in less than 2 seconds!

### Coop
Coop was the quickest. A simple GET request returns a nice `json` file with several product attributes. We grab what we need and go on.

### Lidl
A simple site where we grab the HTML with `requests` and parse it with `lxml`

### Dirk
Another site where `selenium` was the only way to get the product attributes