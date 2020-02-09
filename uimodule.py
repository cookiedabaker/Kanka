### Kanka UI Module ###

### TODO:
### - Add if __name__ = "__main__" functionality

import json, time, re

def jprint(obj):
    """Create a formatted string of the Python JSON object."""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# TODO: Pretty the output, make friendlier to input
# TODO: make broader scope...able to look up a Certain attribute from list of entities.
def search():
    """Search through the data set (names) and return their IDs"""
    entity = [('Name','ID','Entity ID')]
    search_for = input("Search for: ")
    for d in response.json()['data']:
        if re.search(response.json()['data'][d]['name'], search_for):
            name = response.json()['data'][d]['name']
            id = response.json()['data'][d]['id']
            entity_id = response.json()['data'][d]['entity_id']
            entity.append([name, id, entity_id])

    # TODO: Need to add padding/equal spacing to table created.
    print('Entities Found:\r\n')
    for a, b, c, in entity:
        print(a, b, c)
    print('\r\n')


### Main Program ###
exit_program = False
def main():
    global task
    task = input("Task: ").lower()
    if task == "quit" or task == "q":
        return True
    elif task == "get" or task == "post":
        import apicommunicator
        # Need to figure out how to have global variables...
        # Best way may be to just have an init.py file for global variables?
        # May also be useful for passing all the data back and forward...
    elif task == "print":
        jprint(response)
    elif task == 'search':
        search()
    else:
        print('Invalid input.\r\n')

# Run the program
while exit_program == False:
    exit_program = main()

print('Program will now close.')
time.sleep(5)
