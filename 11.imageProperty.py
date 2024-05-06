import cv2 as openCV

imagePath="images/img1.png"
image = openCV.imread(imagePath)

print("Image width:", image.shape[0])
print("Image height:", image.shape[1])
print("Number of channels:", image.shape[2])
print("Image shape:", image.shape)
print("Number of dimensions:", image.ndim) 
print("Image size:", image.size) 
print("Minimum pixel value:", image.min())
print("Maximum pixel value:", image.max())
print("Mean of pixel values:", image.mean())
print("Standard deviation of pixel values:", image.std()) 