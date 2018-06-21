import os
import segmentation
from sklearn.externals import joblib

# load the model
current_dir = os.path.dirname(os.path.realpath(__file__))
model_dir = os.path.join(current_dir, 'models/models/SVC_model.pkl')
model = joblib.load(model_dir)

classification_result = []
for each_character in segmentation.characters:
    each_character = each_character.reshape(1, -1);
    result = model.predict(each_character)
    classification_result.append(result)

print(classification_result)

plate_string = ''
for eachPredict in classification_result:
    plate_string += eachPredict[0]

print(plate_string)
