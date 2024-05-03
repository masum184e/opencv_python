import cv2 as openCV

imagePath="images/img1.png"
image = openCV.imread(imagePath)

print("Image width:", image.shape[0])
print("Image height:", image.shape[1])
print("Number of channels:", image.shape[2])