import cv2 as openCV
import numpy as np

imagePath1="images/img1.png"
imagePath2="images/img2.png"
img1 = openCV.imread(imagePath1)
img2 = openCV.imread(imagePath2)

img1 = openCV.resize(img1, (img2.shape[1], img2.shape[0]))

addition =openCV.add(img1, img2)
subtraction =openCV.subtract(img1, img2)
bitwise_and =openCV.bitwise_and(img1, img2)
bitwise_or =openCV.bitwise_or(img1, img2)
bitwise_xor =openCV.bitwise_xor(img1, img2)
bitwise_not_img2 =openCV.bitwise_not(img2)

openCV.imshow('Image 1', img1)
openCV.imshow('Image 2', img2)
openCV.imshow('Addition', addition)
openCV.imshow('Subtraction', subtraction)
openCV.imshow('Bitwise AND', bitwise_and)
openCV.imshow('Bitwise OR', bitwise_or)
openCV.imshow('Bitwise XOR', bitwise_xor)
openCV.imshow('Bitwise NOT of Image 2', bitwise_not_img2)

openCV.waitKey(0)
openCV.destroyAllWindows()