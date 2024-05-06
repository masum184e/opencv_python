import cv2 as openCV

image1 = openCV.imread('images/img1.png')
image2 = openCV.imread('images/img2.png')

height = min(image1.shape[0], image2.shape[0])
width = min(image1.shape[1], image2.shape[1])
image1 = openCV.resize(image1, (width, height))
image2 = openCV.resize(image2, (width, height))

concatenated_horizontal = openCV.hconcat([image1, image2])
concatenated_vertical = openCV.vconcat([image1, image2])

openCV.imshow('Horizontal Concatenation', concatenated_horizontal)
openCV.imshow('Vertical Concatenation', concatenated_vertical)
openCV.waitKey(0)
openCV.destroyAllWindows()