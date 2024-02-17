import json
import albert_heijn
import jumbo
import aldi
import coop

def save_data(filename, data):
  with open(filename, 'w') as file:
    json.dump(data, file)

supermarkets = {
  'albert-heijn': albert_heijn.main,
  'jumbo': jumbo.main,
  'aldi': aldi.main,
  'coop': coop.main
}

for name, main_function in supermarkets.items():
  data = main_function()
  save_data(f'{name}.json', data)