# discount-scraper

simple scripts that scrape some supermarket sites to see what products are in a discount at the moment. not a lot of functionality, it's mainly a project to figure out what techniques the different sites use with some simple reverse engineering for fun.

## albert heijn

### analysis
- performs a gql request to `https://www.ah.nl/gql`
- `periodStart` and `periodEnd` need to be changed to get the discounts of the current week
- returns a json object where the `titles` are the products that contain a discount

## jumbo
- site does not perform a seperate post request. all the data is seen on the given HTML document
- have to scroll down for all the content to load
- using an XPATH of `//h3/a` is enough to get the titles of products

## aldi
- aldi is crazy. they perform a GET request for every separate article tile on the page
- unloaded divs contain a 'data-tile-url' with the data of the article tile

### method
- using a GET request to get HTML page with discount articles
- extracting data-tile-url's with XPATH
- using GET requests to get the HTML of these pages and extract the article title with XPATH again

## lidl

### analysis
- GET request gets you no content but divs where the article tiles should load contain an attribute 'fulltitle'
- attribute 'fulltitle' contains the name of the article eventhough the content is not loaded

### method
- we can grab the fulltitle attributes of the unloaded article tiles with a simple GET request and XPATH

## coop

### analysis
- they use a API call which returns a JSON with the article titles that are in discount
- API call contains the date of today

### method
- I can recreate the API call and extract the right data

## plus

### analysis
- plus is blocking any request I'm sending and telling me I'm a bot

### method

## todos
- simplify the albert heijn gql query to only ask the data we need
- ah request code needs a function that updates the date variables to the ones of this week
- create a general script that runs all the request scripts of the different sites