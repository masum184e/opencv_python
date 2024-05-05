import cv2 as openCV
import numpy as np

image = 255 * np.ones((512, 512, 3), dtype=np.uint8)

pts = np.array([
        [100, 100], 
        [300, 100], 
        [400, 200], 
        [200, 400]
    ],np.int32
)

isClosed = True
color = (255, 0, 0)
thickness = 2

openCV.polylines(image, [pts], isClosed, color, thickness)

openCV.imshow('Line Image', image)
openCV.waitKey(0)
openCV.destroyAllWindows()
