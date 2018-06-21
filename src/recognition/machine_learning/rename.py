import os
import glob
import string

# Rename letters files
for i in range (65, 91):
    path = 'train/' + chr(i) + '/*.png'
    imgs = glob.glob(path)

    #print(path)
    j = 0
    for x in imgs:
        #print(x.split("/")[2])
        os.rename(x,  'train/' + chr(i) + '/' + chr(i) + '_' + str(j) + '.png')
        j = j + 1

# Rename number files
for i in range (0, 10):
    path = 'train/' + str(i) + '/*.png'
    imgs = glob.glob(path)

    #print(path)
    j = 0
    for x in imgs:
        #print(x.split("/")[2])
        os.rename(x,  'train/' + str(i) + '/' + str(i) + '_' + str(j) + '.png')
        j = j + 1
