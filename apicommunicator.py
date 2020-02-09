### API Communicator ###
"""Handles API communication between UI and Kanka.io database"""

### Still to add:
### - Entity relations
### - Attributes
### - Search/selection ability

import requests

# Campaign specific information
f = open('api.key','r')
api_key = f.read()
f.close()
campaign_id = '19141'

modules = ['characters','locations','families','organizations','items','notes',
    'events','calendars','races','quests','journals','tags','conversations']

# Type of information wanting to be extracted
while True:
    query_type = input('Type of Query: ').lower()
    if query_type == '':
        break
    elif query_type in modules:
        break
    elif query_type == 'dice rolls':
        if query_type != 'dice_rolls':
            query_type = 'dice_rolls'
        break
    else:
        print('Invalid entry.')
        continue

# API querying
url = 'https://kanka.io/api/1.0/campaigns/' + campaign_id + query_type

headers = {
    'Authorization': 'Bearer ' + api_key,
    'Accept': 'application/json'
}

payload = {

}

if task == "get":
    response = requests.get(url, headers=headers, params=payload)
elif task == "post":
    response = requests.post(url, headers=headers, data=payload)

if response.status_code != '200':
    print('The program has encountered a communication problem.')
    print(response.status_code)
