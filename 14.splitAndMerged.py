import cv2 as openCV

imagePath="images/img1.png"
image = openCV.imread(imagePath)

b, g, r = openCV.split(image)
merged_img = openCV.merge((b, g, r))

openCV.imshow('Blue Channel', b)
openCV.imshow('Green Channel', g)
openCV.imshow('Red Channel', r)
openCV.imshow('Merged Image', merged_img)

openCV.waitKey(0)
openCV.destroyAllWindows()