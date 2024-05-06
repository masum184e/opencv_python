import cv2 as openCV
import numpy as np

imagePath="images/img1.png"
image = openCV.imread(imagePath)

flipped_horizontal = openCV.flip(image, 1)
flipped_vertical = openCV.flip(image, 0)
flipped_both = openCV.flip(image, -1)

openCV.imshow('Original Image', image)
openCV.imshow('Flipped Horizontally', flipped_horizontal)
openCV.imshow('Flipped Vertically', flipped_vertical)
openCV.imshow('Flipped Both', flipped_both)

openCV.waitKey(0)
openCV.destroyAllWindows()