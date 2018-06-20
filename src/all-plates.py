import numpy as np
import cv2
import sys
import os
from operator import itemgetter

#frame = cv2.imread(sys.argv[1], cv2.IMREAD_COLOR)
#frame = cv2.pyrMeanShiftFiltering(frame, 31, 91)
qt_characters = 10
if not os.path.exists("output"):
    os.makedirs("output")

if not os.path.exists("output/all_outputs"):
    os.makedirs("output/all_outputs")

path = "./../imagesALPR/"
files = os.listdir(path)
for file2 in files:
    print(file2)
    file3 = file2.split('.')
    file = file3[0]
    frame = cv2.imread(path + file2, cv2.IMREAD_COLOR)
    gray_frame = cv2.cvtColor( frame, cv2.COLOR_RGB2GRAY )
    median_noise_reduction = cv2.medianBlur(gray_frame, 3)

    kernel = np.ones((3,3),np.uint8)
    eroded_frame = cv2.erode(median_noise_reduction, kernel, iterations = 1)
    dilated_frame = cv2.dilate(median_noise_reduction, kernel, iterations = 1)

    new_frame = dilated_frame - eroded_frame

    kernel2 = np.ones((1, 70), np.uint8)

    eroded_frame2 = cv2.erode(new_frame, kernel2, iterations = 1)
    new_frame =  new_frame - eroded_frame2

    h, w = new_frame.shape[:2]
    mask = np.zeros((h+2, w+2), np.uint8)

    (thresh, im_bw) = cv2.threshold(new_frame, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    new_frame2 = im_bw.copy()

    cv2.floodFill(new_frame2, mask, (0,0), 255)

    new_frame2 = 255-new_frame2
    #new_frame2 = cv2.erode(new_frame2, kernel, iterations = 1)
    #new_frame2 = cv2.dilate(new_frame2, kernel, iterations = 1)

    if not os.path.exists("output/" + file):
	    os.makedirs("output/" + file)

    _, contours,_ = cv2.findContours(new_frame2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    imgsvector = []
    qt_characters = 7
    for contour in contours:
    	area = cv2.contourArea(contour)
    	if area > 250:
    		#cv2.drawContours(frame,contour,-1,(0,0,255),3) #desenha o contorno. Linha comentada pois estou desenhando retangulos em baixo

    		#rect = cv2.minAreaRect(contour) #pega o retangulo minimo
    		#box = cv2.boxPoints(rect) #pontos da box
    		#box = np.int0(box) #converte pra int0
    		#if abs(box[0][0]-box[2][0])>70: continue #se a largura for maior que 70
    		#cv2.drawContours(frame,[box],-1,(0,255,0),1) #desenha
    		x,y,w,h = cv2.boundingRect(contour) #boundingboxes
    		if w > (2*h):
    			continue
    		cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2) #desenha retangulo
    		crop_img = new_frame2[y:y+h, x:x+w] #corta o retangulo
    		numero = x+y #variavel pra controlar o nome dos caracteres segmentados
    		crop_imgTuple = (area, crop_img, numero)
    		imgsvector.append(crop_imgTuple)

    imgsvector = sorted(imgsvector, key=itemgetter(0), reverse=True)
    imgsvector = imgsvector[0:qt_characters]
    imgsvector = sorted(imgsvector, key=itemgetter(2))

    for imgpos in imgsvector:
        cv2.imwrite("output/"+ file + "/" + str(imgpos[2]) + ".png", imgpos[1])

    cv2.imwrite("output/" + file + "/" + file + "1.jpg", new_frame2)
    cv2.imwrite("output/" + file + "/" + file + "2.jpg", frame)
    cv2.imwrite("output/all_outputs/" + file + ".jpg", new_frame2)
    #cv2.drawContours(frame,contours,-1,(0,0,255),6)
    #cv2.imshow('NEW_IMAGE', frame)
cv2.waitKey(0)
