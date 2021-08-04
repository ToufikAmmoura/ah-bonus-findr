import os
import requests
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

def gettingBonusDiv():
    r = requests.get('https://www.ah.nl/bonus')
    soup = BeautifulSoup(r.content, 'html.parser')
    k = soup.find_all(name='span')
    print(k)

    # b = soup.find('a', class_='link_root__3u9Oq product-card-portrait_link__2ctJY', recursive=True)
    # print(b)


def main():
    rds = parsingRobotsTxt()
    allowed = checkingRobotsTxt(rds)
    if allowed:
        gettingBonusDiv()

main()