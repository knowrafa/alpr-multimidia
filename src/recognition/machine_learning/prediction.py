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
    j = 1
    for eachPredict in classification_result:

        # Analise de contexto
        if(j <= 3):
            if (str(eachPredict[0]).split("'")[1]) == "0":
                 plate_string += "O"
            elif (str(eachPredict[0]).split("'")[1]) == "1":
                plate_string += "I"
            elif (str(eachPredict[0]).split("'")[1]) == "2":
                plate_string += "Z"
            elif (str(eachPredict[0]).split("'")[1]) == "8":
                plate_string += "B"
            else:
                plate_string += (str(eachPredict[0]).split("'")[1])
        else:
            if (str(eachPredict[0]).split("'")[1]) == "D":
                plate_string += "0"
            elif (str(eachPredict[0]).split("'")[1]) == "T":
                plate_string += "1"
            elif (str(eachPredict[0]).split("'")[1]) == "Z":
                plate_string += "2"
            elif (str(eachPredict[0]).split("'")[1]) == "B":
                plate_string += "8"
            elif (str(eachPredict[0]).split("'")[1]) == "S":
                plate_string += "5"
            else:
                plate_string += (str(eachPredict[0]).split("'")[1])

        j = j + 1
    # Nome da pasta da placa + a placa que foi reconhecida
    print(folder.split("/")[3] + '\t' + plate_string + "\n\n")
