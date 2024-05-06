import cv2 as openCV

image = openCV.imread('images/img1.png', openCV.IMREAD_GRAYSCALE)

threshold1 = 100
threshold2 = 200

edges = openCV.Canny(image, threshold1, threshold2)

openCV.imshow('Original Image', image)
openCV.imshow('Edges Detected', edges)
openCV.waitKey(0)
openCV.destroyAllWindows()