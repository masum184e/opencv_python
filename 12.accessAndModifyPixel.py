import cv2 as openCV

imagePath="images/img1.png"
image = openCV.imread(imagePath)

print("Pixel value at (100, 100):", image[100][100])

image[100, 100] = [255, 255, 255] 
image[101, 101] = [255, 255, 255] 
image[102, 102] = [255, 255, 255] 
image[103, 103] = [255, 255, 255] 
image[104, 104] = [255, 255, 255] 
image[105, 105] = [255, 255, 255] 
image[106, 106] = [255, 255, 255] 
image[107, 107] = [255, 255, 255] 
image[108, 108] = [255, 255, 255] 
image[109, 109] = [255, 255, 255] 
image[110, 110] = [255, 255, 255] 

# Numpy is an optimized library for fast array calculations. So simply accessing each and every pixel value and modifying it will be very slow and it is discouraged.

# image.item(10,10,2) -> accessing RED value of index [10, 10], 0 for blue, 1 for green
# image.itemset((10,10,2),100) -> modifying RED value of index [10, 10]

openCV.imshow('Image', image)
openCV.waitKey(0)
openCV.destroyAllWindows()