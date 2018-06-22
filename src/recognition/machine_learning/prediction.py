import os
#import segmentation
from sklearn.externals import joblib
import glob
from skimage.io import imread
from skimage.transform import resize

def segmentation (path):
    cpath = path + '/*.png'

    imgs = glob.glob(cpath)
    characters = []

    for x in imgs:
        car_image = imread(x, as_gray=True)
        resized_char = resize(car_image, (20, 20))
        characters.append(resized_char)

    return characters


# load the model
current_dir = os.path.dirname(os.path.realpath(__file__))
model_dir = os.path.join(current_dir, 'models/svc/SVC_model.pkl')
model = joblib.load(model_dir)

path = '../../output/*'
ppath = glob.glob(path)

for folder in ppath:
    classification_result = []
    character = segmentation(folder)
    for each_character in character:
        each_character = each_character.reshape(1, -1);
        result = model.predict(each_character)
        classification_result.append(result)

    # print(classification_result)

    plate_string = ''
    for eachPredict in classification_result:
        #plate_string += (eachPredict[0])
        plate_string += (str(eachPredict[0]).split("'")[1])

    print(folder.split("/")[3] + '\t' + plate_string + "\n\n")
