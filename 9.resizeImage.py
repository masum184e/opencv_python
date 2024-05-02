import cv2 as openCV
import numpy as np

imagePath="images/img1.png"
image = openCV.imread(imagePath)

new_width = 400
new_height = 300
resized_image = openCV.resize(image, (new_width, new_height))

scale_factor = 0.5
scaled_image = openCV.resize(image, None, fx=scale_factor, fy=scale_factor)

openCV.imshow('Original Image', image)
openCV.imshow('Resized Image', resized_image)
openCV.imshow('Scaled Image', scaled_image)

openCV.waitKey(0)
openCV.destroyAllWindows()