import cv2 as openCV

imagePath="images/img1.png"
image = openCV.imread(imagePath)

x, y, w, h = 100, 100, 200, 150
roi = image[y:y+h, x:x+w] 

openCV.imshow('ROI', roi)
openCV.waitKey(0)
openCV.destroyAllWindows()