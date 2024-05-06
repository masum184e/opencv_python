import cv2 as cv
import numpy as np

imagePath="images/img1.png"
img = cv.imread(imagePath)

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = cv.inRange(hsv_img, lower_blue, upper_blue)
blue_object = cv.bitwise_and(img, img, mask=mask)
blurred_image = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

cv.imshow('Original Image', img)
cv.imshow('Grayscale Image', gray_img)
cv.imshow('Blur Image', blurred_image)
cv.imshow('HSV Image', hsv_img)
cv.imshow('Extracted Blue Object', blue_object)

cv.waitKey(0)
cv.destroyAllWindows()
