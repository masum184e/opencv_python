import cv2 as openCV

imagePath="images/img1.png"
image = openCV.imread(imagePath)

x, y, w, h = 100, 100, 200, 150
roi = image[y:y+h, x:x+w] 

openCV.imshow('ROI', roi)
openCV.waitKey(0)
openCV.destroyAllWindows()

# For eye detection in images, first face detection is done over the entire image.
# When a face is obtained, we select the face region alone and search for eyes inside it instead of searching the whole image.
# It improves accuracy (because eyes are always on faces :D ) and performance (because we search in a small area).