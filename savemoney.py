import os
import requests
import re

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
    rules = ['/bonus', '/bonus/']
    allowed = True
    for rule in result_data_set['Disallowed']:
        if rule in rules:
            return False
    return allowed

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
    rds = parsingRobotsTxt()
    allowed = checkingRobotsTxt(rds)
    if allowed:
        titles, date = parseSite()
        discount = checkProducts(titles)
        print(f'Products with a discount for {date}:\n', discount)

main()