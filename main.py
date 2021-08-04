import os
import requests
import re
from bs4 import BeautifulSoup

def parsingRobotsTxt():
    result = os.popen("curl -s https://www.ah.nl/robots.txt").read()
    result_data_set = {"Disallowed":[], "Allowed":[]}

    for line in result.split("\n"):
        if line.startswith('Allow'):    # allowed urls
            result_data_set["Allowed"].append(line.split(' ')[1])
        elif line.startswith('Disallow'):    # disallowed urls
            if len(line.split(' ')) > 1:
                result_data_set["Disallowed"].append(line.split(' ')[1])
    
    return result_data_set

def checkingRobotsTxt(result_data_set):
    var1, var2 = '/bonus', '/bonus/'
    allowed = True
    for el in result_data_set['Disallowed']:
        if el == var1 or el == var2:
            return False
    return allowed

def gettingTitles():
    r = requests.get('https://www.ah.nl/bonus')
    con = str(r.content)
    occurences = [m.start() for m in re.finditer('"title":', con)]
    titles = []
    for o in occurences:
        s = o + len('"title":') + 1
        title = ""
        while con[s] != '"':
            title += con[s]
            s += 1
        if title:
            titles.append(title)
    return set(titles)

def checkProducts(titles):
    products = ['AH Kleine salades en pastasalades', 'AH Amandeldrink', 'Quaker Havermout']
    for t in titles:
        for p in products:
            if p in t:
                print(p)


def main():
    rds = parsingRobotsTxt()
    allowed = checkingRobotsTxt(rds)
    if allowed:
        ts = gettingTitles()
        checkProducts(ts)


main()