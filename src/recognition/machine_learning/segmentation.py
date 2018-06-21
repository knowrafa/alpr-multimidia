import glob
from skimage.io import imread
from skimage.transform import resize


path = 'character/*.png'
imgs = glob.glob(path)
characters = []

for x in imgs:
    car_image = imread(x, as_gray=True)
    resized_char = resize(car_image, (20, 20))
    characters.append(resized_char)
