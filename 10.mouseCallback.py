import cv2 as openCV
import numpy as np

image = 255 * np.ones((512, 512, 3), dtype=np.uint8)

radius = 20
color = (255, 0, 0)
thickness = -1

def draw_circle(event, x, y, flags, param):
    if event == openCV.EVENT_LBUTTONDOWN:
        center_coordinates = (x, y)
        openCV.circle(image, center_coordinates, radius, color, thickness)

openCV.namedWindow('image')
openCV.setMouseCallback('image', draw_circle)

while True:
    openCV.imshow('image', image)
    if openCV.waitKey(20) & 0xFF == 27:
        break

openCV.destroyAllWindows()