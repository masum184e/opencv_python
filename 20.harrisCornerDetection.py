import cv2 as openCV
import numpy as np

imagePath="images/img1.png"
image = openCV.imread(imagePath)

gray = openCV.cvtColor(image, openCV.COLOR_BGR2GRAY)

block_size = 2
ksize = 3
k = 0.04
dst = openCV.cornerHarris(gray, block_size, ksize, k)

threshold = 0.01 * dst.max()

image[dst > threshold] = [0, 0, 255]

openCV.imshow('Harris Corner Detection', image)
openCV.waitKey(0)
openCV.destroyAllWindows()
