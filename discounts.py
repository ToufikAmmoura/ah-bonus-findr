import json
from datetime import date
import os

import albert_heijn
import jumbo
import aldi
import coop
import lidl
import dirk

def save_data(filename, data):
  with open(filename, 'w') as file:
    json.dump(data, file)

supermarkets = {
  'albert-heijn': albert_heijn.main,
  'jumbo': jumbo.main,
  'aldi': aldi.main,
  'coop': coop.main,
  'lidl': lidl.main,
  'dirk': dirk.main
}

for name, main_function in supermarkets.items():
  data = main_function()
  
  today_date = date.today().strftime('%d-%m-%Y')
  new_dir_path = f'discount_data/{today_date}'
  os.makedirs(new_dir_path, exist_ok=True)
  
  save_data(f'discount_data/{today_date}/{name}.json', data)