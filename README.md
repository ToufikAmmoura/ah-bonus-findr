# discount-scraper

simple scripts that scrape some supermarket sites to see what products are in a discount at the moment. not a lot of functionality, it's mainly a project to figure out what techniques the different sites use with some simple reverse engineering for fun.

## albert heijn

### analysis
- performs a gql request to `https://www.ah.nl/gql`
- `periodStart` and `periodEnd` need to be changed to get the discounts of the current week
- returns a json object where the `titles` are the products that contain a discount

## jumbo

## aldi

## lidl

## todos
- simplify the albert heijn gql query to only ask the data we need