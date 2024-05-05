import cv2 as openCV

imagePath = "images/img1.png"
image = openCV.imread(imagePath, openCV.IMREAD_GRAYSCALE)

_, simple_threshold = openCV.threshold(image, 127, 255, openCV.THRESH_BINARY)
adaptive_threshold = openCV.adaptiveThreshold(image, 255, openCV.ADAPTIVE_THRESH_MEAN_C, openCV.THRESH_BINARY, 11, 2)
_, otsu_threshold = openCV.threshold(image, 0, 255, openCV.THRESH_BINARY + openCV.THRESH_OTSU)

simple_threshold = simple_threshold.astype('uint8')
adaptive_threshold = adaptive_threshold.astype('uint8')
otsu_threshold = otsu_threshold.astype('uint8')

openCV.imshow('Original Image', image)
openCV.imshow('Simple Thresholding', simple_threshold)
openCV.imshow('Adaptive Thresholding', adaptive_threshold)
openCV.imshow("Otsu's Thresholding", otsu_threshold)

openCV.waitKey(0)
openCV.destroyAllWindows()
