import xml.etree.ElementTree as ET
import json
import yaml

x = open('db.json')
data = json.load(x)
for i in data:
    print(data[i])

x.close()    

with open('db.yml') as f:
    
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)


tree = ET.parse('db.xml')
root = tree.getroot()

for elem in root:
   for subelem in elem:
      print(subelem.text)


import json
#opening dnac_devices.json file
with open("dnac_devices.json") as f:
    json_data = json.load(f)
#displaying data
for item in json_data["response"]:
    print(item["id"])
    print(item["type"])
    print(item["family"])
    print(item["softwareType"])
    print(item["managementIpAddress"])
    print()

