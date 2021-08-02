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

    f = open('text.txt', 'w', encoding='utf-8')
    f.write(str(soup.find_all(text=True)))
    f.close()

    bonusen = soup.find_all('div', class_='grid_spanFrom-lg-2__1fBvP', recursive=True)
    
    f = open('text2.txt', 'w', encoding='utf-8')
    f.write(str(bonusen.find_all(text=True)))
    f.close()


def main():
    rds = parsingRobotsTxt()
    allowed = checkingRobotsTxt(rds)
    if allowed:
        gettingBonusDiv()

main()