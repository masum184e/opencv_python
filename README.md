## Installation
```
pip install opencv-python
```

## Read
- `openCV.imread(imagePath)` - load the image from the specified path

- `openCV.imshow(frameName, image)` - display an image in a window

- `openCV.waitKey(0)` - 
- `openCV.destroyAllWindows()` - 

## Draw Line
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