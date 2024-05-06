import cv2
import numpy as np

image = cv2.imread('images/img1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

contour_image = np.copy(image)
cv2.drawContours(contour_image, contours, -1, (0, 0, 255), 2)

cv2.imshow('Original Image', image)
cv2.imshow('Contours', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
