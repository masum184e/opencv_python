import cv2 as openCV
import numpy as np

image = openCV.imread('images/img1.png', openCV.IMREAD_GRAYSCALE)

kernel = np.ones((5,5), np.uint8)

erosion = openCV.erode(image, kernel, iterations=1)
dilation = openCV.dilate(image, kernel, iterations=1)
opening = openCV.morphologyEx(image, openCV.MORPH_OPEN, kernel)
closing = openCV.morphologyEx(image, openCV.MORPH_CLOSE, kernel)

openCV.imshow('Original Image', image)
openCV.imshow('Erosion', erosion)
openCV.imshow('Dilation', dilation)
openCV.imshow('Opening', opening)
openCV.imshow('Closing', closing)
openCV.waitKey(0)
openCV.destroyAllWindows()
