import cv2 as cv
import numpy as np

image = 255 * np.ones((512, 512, 3), dtype=np.uint8)

center_coordinates = (256, 256)
axes_length = (200, 100)
angle = 0 
startAngle = 0
endAngle = 360 
color = (255, 0, 0)
thickness = 2

cv.ellipse(image, center_coordinates, axes_length, angle, startAngle, endAngle, color, thickness)

cv.imshow('Ellipse Image', image)
cv.waitKey(0)
cv.destroyAllWindows()
