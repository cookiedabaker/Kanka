### Kanka UI Module ###

import json
import time

def jprint(obj):
    """Create a formatted string of the Python JSON object."""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

exit_program = False
def main():
    task = input("Task: ").lower()
    if task == "quit" or task == "q":
        return True
    elif task == "get" or task == "post":
        import apicommunicator
        # Need to figure out how to have global variables...
    else:
        print('Invalid input.')

while exit_program == False:
    exit_program = main()

print('Program will now close.')
time.sleep(5)
