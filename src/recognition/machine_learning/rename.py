import os
import glob
import string

#path = 'train/0/*.png'
#imgs = glob.glob(path)
#characters = []

for i in range (65, 91):
    path = 'train/' + chr(i) + '/*.png'
    imgs = glob.glob(path)

    #print(path)
    j = 0
    for x in imgs:
        #print(x.split("/")[2])
        os.rename(x,  'train/' + chr(i) + '/' + chr(i) + '_' + str(j) + '.png')
        j = j + 1
