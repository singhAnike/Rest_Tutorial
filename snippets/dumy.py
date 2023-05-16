# Lts understand littile bit about json
import json

d = {'name': 'Aniket Singh', 'roll': 10}
serialized_data = json.dumps(d)

with open("snippets/output.json", "w") as fp:
    fp.write(serialized_data)


# This is the use to check our current working path 
import os

print(os.getcwd())