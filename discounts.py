import json
import albert_heijn
import jumbo

def save_data(filename, data):
  with open(filename, 'w') as file:
    json.dump(data, file)

ah_data = albert_heijn.main()
save_data('albert-heijn.json', ah_data)

jumbo_data = jumbo.main()
save_data('jumbo.json', jumbo_data)



