import requests
import json
req = requests.get('http://worldtimeapi.org/api/timezone/asia/Kolkata.json').text
data =  json.loads(req)
print(data['datetime'])
