import cv2 as openCV
import numpy as np

imagePath="images/img1.png"
image = openCV.imread(imagePath)

height, width = image.shape[:2]

angle = 45
rotation_matrix = openCV.getRotationMatrix2D((width / 2, height / 2), angle, 1)

rotated_img = openCV.warpAffine(image, rotation_matrix, (width, height))

openCV.imshow('Original Image', image)
openCV.imshow('Rotated Image', rotated_img)

openCV.waitKey(0)
openCV.destroyAllWindows()