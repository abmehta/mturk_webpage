#Access json file to understand format
import json
with open('../setlist.json') as f:
    data = json.load(f)

print data['6000']