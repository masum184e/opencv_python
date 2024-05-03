import cv2 as openCV
import numpy as np

imagePath="images/img1.png"
image = openCV.imread(imagePath)

height, width = image.shape[:2]

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
affine_matrix = openCV.getAffineTransform(pts1, pts2)

affine_img = openCV.warpAffine(image, affine_matrix, (width, height))

openCV.imshow('Original Image', image)
openCV.imshow('Affine Transformed Image', affine_img)

openCV.waitKey(0)
openCV.destroyAllWindows()