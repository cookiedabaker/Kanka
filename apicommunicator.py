### API Communicator ###
"""Handles API communication between UI and Kanka.io database"""

### Still to add:
### - Entity relations
### - Attributes
### - Search/selection ability

import requests
import json
import time

# Campaign specific information
api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImZmZjMzY2Y3NjU1Mjk3NmZjZmRhNmYzMzEyNDg2OWM4YWQ2NTU2NTkxOWIxYTg1NWMzYzU1ZGIyOTFkZTViMzJjNDE1ODQ0MGYxN2NlZmQwIn0.eyJhdWQiOiIxIiwianRpIjoiZmZmMzNjZjc2NTUyOTc2ZmNmZGE2ZjMzMTI0ODY5YzhhZDY1NTY1OTE5YjFhODU1YzNjNTVkYjI5MWRlNWIzMmM0MTU4NDQwZjE3Y2VmZDAiLCJpYXQiOjE1ODA2ODQwNjcsIm5iZiI6MTU4MDY4NDA2NywiZXhwIjoxNjEyMzA2NDY3LCJzdWIiOiIyMjAyMyIsInNjb3BlcyI6W119.MWn_ebZejLQ_xVbmP89Kl8WkPlnHZ9e1w1ZJZ4HqKDy9s9OSo_BJdYxozHcO4ELvGXVa50QFl4buszx_j0Fd4IcvfixBrBH5k_l0aynJloyItW55RhHwomKUuGeh4ZAVZ9Mi8_6-87V7qTmGSDCFns9YT4216btW2WOJdPEuO-h4xpvuBzY8gR9NZ7fPHkpDe4SEqqNJaiDCNAsAzhFF-k5FWtZJXD9lnwWekagnhnw7yZ2k09_b2ZUL3JZTyi2LUkzcB0Dvsprnj1GWofWjmauAm2H2YtRuBX34zQoKjmBbhCjjeT0WHXvGR2DFdow70LPnc2u1-oy_BjqABbsk6-qG3AtenrOA35AhW9l40_A4m1iZg5Oe7qB6ksj2fwH-ZXwL8mDjpiYZtPYch95urq-6EGcSde0iTLTixmYK7WAUurhbHnUduAldBUshK0ZWPodQ8Y25-Q_rRZ8RkiYq3JPS6aBNFF43_2X7MBl6NotIZQzuM03NMB3rhEbeERALALyiDMYN6fve7O0nQW0OuXECIsa3Tmo885YeoVwFszRKs9rtg4PUFA1G0s6SDETMnQrFloiz-zDjW1fhgukCDiwjAQsZnEhcKmucxYQPDtfIz5NEu3bHmIzDIKCt7cHhhYf2wVv45WZS3KXsUDP0Otvg7bViZrs_QemkiJABlEM"
campaign_id = '19141'

# Type of information wanting to be extracted
while true:
    query_type = input('Type of Query (lowercase):')
    if query_type == '':
        break
    elif query_type == 'characters':
        break
    elif query_type == 'locations':
        break
    elif query_type == 'families':
        break
    elif query_type == 'organizations':
        break
    elif query_type == 'items':
        break
    elif query_type == 'notes':
        break
    elif query_type == 'events':
        break
    elif query_type == 'calendars':
        break
    elif query_type == 'races':
        break
    elif query_type == 'quests':
        break
    elif query_type == 'journals':
        break
    elif query_type == 'tags':
        break
    elif query_type == 'conversations':
        break
    elif query_type == 'dice rolls':
        if query_type != 'dice_rolls':
            query_type = 'dice_rolls'
        break
    else:
        print('Invalid entry.')
        continue

url = 'https://kanka.io/api/1.0/campaigns/' + campaign_id + query_type

headers = {
    'Authorization': 'Bearer ' + api_key,
    'Accept': 'application/json'
}

payload = {

}

response = requests.get(url, headers=headers, params=payload)

if response.status_code != '200':
    print('The program has encountered a communication problem.')
    print(response.status_code)

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)
