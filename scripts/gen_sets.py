#Generate sets of 8 images 
from random import randint
import json

#Read in file names
#filenames = pd.readcsv('../get_labels_meters.csv',nrows=2000, usecols=['filename'])

setlist = []
counter = 1

for i in xrange(6000):
    curr_set = []
    for j in xrange(8):
        curr_set.append(randint(1,2000))
    setlist.append({counter:curr_set})
    counter += 1

with open('../setlist.json','w') as opfile:
    json.dump(setlist, opfile)
#print setlist[:10]