import cv2 as openCV

# imagePath=input("Enter Your Image Path: ")
imagePath="images/img1.png"
image = openCV.imread(imagePath)

if image is not None:
    openCV.imshow('Image', image)
    openCV.waitKey(0)
else:
    print("Failed to load the image.")
