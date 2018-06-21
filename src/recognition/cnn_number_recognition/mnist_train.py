import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint
from keras.models import load_model
from keras.layers import GlobalAveragePooling2D, Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten, Activation
from keras.datasets import mnist
from keras.utils import np_utils
num_classes = 10
IMAGE_SIZE = 28
# the data, shuffled and split between tran and test sets
(X_train, y_train), (X_test, y_test) = mnist.load_data()

X_train = X_train.reshape(X_train.shape[0], 28, 28, 1)
X_test = X_test.reshape(X_test.shape[0], 28, 28, 1)

X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255
Y_train = np_utils.to_categorical(y_train, 10)
Y_test = np_utils.to_categorical(y_test, 10)


def cnn_model():

    model = Sequential()

    model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(IMAGE_SIZE,IMAGE_SIZE,1)))
    model.add(Conv2D(32, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))


    model.add(Conv2D(64, (3, 3), activation='relu', padding='same'))
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())

    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))

    model.add(Dense(num_classes, activation='softmax'))

    model.summary()


    return model

'''
model = cnn_model()
checkpoint = ModelCheckpoint('mnist_digits.h5',  # model filename
                         monitor='val_loss', # quantity to monitor
                         verbose=0, # verbosity - 0 or 1
                         save_best_only= True, # The latest best model will not be overwritten
                         mode='auto') # The decision to overwrite model is made
                                      # automatically depending on the quantity to monitor

model.compile(loss='categorical_crossentropy', # Better loss function for neural networks
              optimizer=Adam(lr=1.0e-4), # Adam optimizer with 1.0e-4 learning rate
              metrics = ['accuracy']) # Metrics to be evaluated by the model

model_details = model.fit(X_train, Y_train,
                batch_size = 32, # number of samples per gradient update
                epochs = 10, # number of iterations
                validation_data= (X_test, Y_test),
                callbacks=[checkpoint],
                verbose=1)

score = model.evaluate(X_test, Y_test, verbose=0)
print('Test score:', score[0])
print('Test accuracy:', score[1])
'''

modelo = load_model('mnist_digits.h5')
scores = modelo.evaluate(X_test, Y_test, verbose = 0)
print('Accuracy: %.2f%%' % (scores[1]*100))
teste = X_test[10].reshape(1, 28, 28, 1)
print(modelo.predict(teste))
pixels = teste
pixels = pixels.reshape((28,28))
plt.imshow(pixels, cmap = 'gray')
plt.show()
