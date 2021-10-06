import os
import requests
import re

def parseSite():
    def getTitles(con):
        occurences = [m.start() for m in re.finditer('"title":', con)]
        titles = []
        for o in occurences:
            s = o + len('"title":') + 1
            title = ""
            while con[s] != '"':
                title += con[s]
                s += 1
            if title:
                titles.append(title.lower())
        return set(titles)

    def getDate(con):
        index = con.find('t/m')
        date = con[index-2:index+10]
        return date

    r = requests.get('https://www.ah.nl/bonus')
    content = str(r.content)
    return getTitles(content), getDate(content)
    
def checkProducts(titles):
    products = ['ah kleine salades en pastasalades', 'amandeldrink', 'quaker havermout', 'bramen', 'breaker']
    bonus = []
    for t in titles:
        for p in products:
            if p in t:
                bonus.append(t.replace('\\', ''))
    return bonus

def main():
    titles, date = parseSite()
    discount = checkProducts(titles)
    print(f'Products with a discount for {date}:\n', discount)

main()