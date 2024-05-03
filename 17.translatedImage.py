import cv2 as openCV
import numpy as np

imagePath="images/img1.png"
image = openCV.imread(imagePath)

height, width = image.shape[:2]

tx = 100 
ty = 50
translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])

translated_img = openCV.warpAffine(image, translation_matrix, (width, height))

openCV.imshow('Original Image', image)
openCV.imshow('Translated Image', translated_img)

openCV.waitKey(0)
openCV.destroyAllWindows()