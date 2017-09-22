#Generate sets of 8 images 
from random import randint
import json

#Read in file names
#filenames = pd.readcsv('../get_labels_meters.csv',nrows=2000, usecols=['filename'])

with open('../setoflist.txt','w') as opfile:
    for i in xrange(6000):
        curr = i
        opfile.write("%s," % str(curr))
        for j in xrange(7):
            curr += 10
            if j==6:
                opfile.write("%s" % str(curr))
            else:
                opfile.write("%s," % str(curr))
        opfile.write("\n")
        
#print setlist[:10]