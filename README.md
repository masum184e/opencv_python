## Installation
```
pip install opencv-python
```

## Read
- `openCV.imread(imagePath)` - load the image from the specified path

- `openCV.imshow(frameName, image)` - display an image in a window

- `openCV.waitKey(0)` -  allows users to display a window for given milliseconds or until any key is pressed. If the parameter value is 0, you have press any key from your keyboard to destroy the window, untill it will keep open. If the parameter value is other value instead of 0, it will automatically destroy the window after that amount of milliseconds

- `openCV.destroyAllWindows()` - close all open window. [View More](https://www.geeksforgeeks.org/python-opencv-destroyallwindows-function/)

- `destroyWindow(windName)` - close a specif window

## Draw Line
- `dtype=np.uint8` - specifies the data type of the elements in the array.
- `np.zeros((3, 3))` - creates a 3x3 array filled with zeros
- `np.ones((3, 3))` - creates a 3x3 array filled with ones
- `np.full((2, 2), 5)` - creates a 2x2 array filled with the value 5
- `np.empty((2, 2))` - creates a 2x2 uninitialized array
- `np.eye(3)` or `np.identity(3)` - creates a 3x3 identity matrix
- `np.ones((512, 512, 3))` - creates 512x512 array which filled with 1x3 array which is filled with the value 1
- `255*np.ones((512, 512, 3))` - 

```
import cv2 as openCV
import numpy as np

image = 255 * np.ones((512, 512, 3), dtype=np.uint8)

start_point = (100, 100)
end_point = (400, 400)
color = (255, 0, 0)
thickness = 2

openCV.line(image, start_point, end_point, color, thickness)

openCV.imshow('Line Image', image)
openCV.waitKey(0)
openCV.destroyAllWindows()

``` 
![Line](/images/drawLine.jpg)

## Draw Circle
```
import cv2 as openCV
import numpy as np

image = 255 * np.ones((512, 512, 3), dtype=np.uint8)

center_coordinates = (256, 256)
radius = 100
color = (255, 0, 0)
thickness = 2

openCV.circle(image, center_coordinates, radius, color, thickness)

openCV.imshow('Line Image', image)
openCV.waitKey(0)
openCV.destroyAllWindows()
```
![Circle](/images/drawCircle.jpg)

## Draw Ellipse
```
import cv2 as openCV
import numpy as np

image = 255 * np.ones((512, 512, 3), dtype=np.uint8)

center_coordinates = (256, 256)
axes_length = (200, 100)
angle = 0 
startAngle = 0
endAngle = 360 
color = (255, 0, 0)
thickness = 2

openCV.ellipse(image, center_coordinates, axes_length, angle, startAngle, endAngle, color, thickness)

openCV.imshow('Ellipse Image', image)
openCV.waitKey(0)
openCV.destroyAllWindows()
```
![Ellipse](/images/drawEllipse.jpg)