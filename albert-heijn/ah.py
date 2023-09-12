import json
from datetime import datetime, timedelta
from ah_request import get_bonus

def get_date():
    # getting the date of the monday of this week
    now = datetime.now()
    monday = now - timedelta(days = now.weekday())
    return monday.strftime('%d-%m')

WISHES = ['ah kleine salades en pastasalades', 'amandeldrink', 'quaker havermout', 'bramen', 'breaker']

response = get_bonus()
data = response.json()

with open ('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

discounts = [el['title'].lower() for el in data[0]['data']['bonusSegments']]

for d in discounts:
    print(d)
#     for w in WISHES:
#         if w in d:
#             print(d)

# parser = argparse.ArgumentParser()
# parser.add_argument('-debug', action='store_true')
# args = parser.parse_args()

# if args.debug:
#     for d in discounts:
#         print(d)

# title = f'bonus-{get_date()}.txt'
# f = open(title, 'w')
# for d in discounts:
#     f.write(d+'\n')
# f.close()

