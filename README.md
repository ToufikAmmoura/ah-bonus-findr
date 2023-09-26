# discount-scraper

simple scripts that scrape some supermarket sites to see what products are in a discount at the moment. not a lot of functionality, it's mainly a project to figure out what techniques the different sites use with some simple reverse engineering for fun.

## albert heijn

### analysis
- performs a gql request to `https://www.ah.nl/gql`
- `periodStart` and `periodEnd` need to be changed to get the discounts of the current week
- returns a json object where the `titles` are the products that contain a discount

## jumbo
- site does not perform a seperate post request. all the data is seen on the given HTML document
- using an XPATH of `//h3/a` is enough to get the titles of products

## aldi

## lidl

## todos
- simplify the albert heijn gql query to only ask the data we need
- ah request code needs a function that updates the date variables to the ones of this week
- create a general script that runs all the request scripts of the different sites