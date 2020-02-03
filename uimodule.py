### Kanka UI Module ###

### TODO:
### - Add if __name__ = "__main__" functionality

import json
import time
import re
from tabulate import tabulate

def jprint(obj):
    """Create a formatted string of the Python JSON object."""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

def search():
    # TODO: Pretty the output, make friendlier to input
    entity = [('Name','ID','Entity ID')]
    search_for = input("Search for: ")
    for d in response.json()['data']:
        if re.search(response.json()['data'][d]['name'], search_for):
            name = response.json()['data'][d]['name']
            id = response.json()['data'][d]['id']
            entity_id = response.json()['data'][d]['entity_id']
            entity.append(name, id, entity_id)

    print('Entities Found:\r\n')
    for a, b, c, in entity:
        print(a, b, c)
    print('\r\n')

exit_program = False
def main():
    task = input("Task: ").lower()
    if task == "quit" or task == "q":
        return True
    elif task == "get" or task == "post":
        import apicommunicator
        # Need to figure out how to have global variables...
    elif task == 'search':
        search()
    else:
        print('Invalid input.\r\n')


while exit_program == False:
    exit_program = main()

print('Program will now close.')
time.sleep(5)
