# Introduction
OpenCV (Open Source Computer Vision Library) is an open-source computer vision and machine learning software library. It provides a wide variety of tools and functions that help in tasks such as image and video processing, object detection, motion tracking, and more.

OpenCV-Python is the Python wrapper for OpenCV. It allows you to use OpenCV's C++ library functions in Python scripts. OpenCV-Python is well-suited for fast prototyping of computer vision applications.

Compared to languages like C/C++, Python is slower. That said, Python can be easily extended with C/C++, which allows us to write computationally intensive code in C/C++ and create Python wrappers that can be used as Python modules. This gives us two advantages: first, the code is as fast as the original C/C++ code (since it is the actual C++ code working in background) and second, it is easier to code in Python than C/C++. OpenCV-Python is a Python wrapper for the original OpenCV C++ implementation.

OpenCV-Python makes use of Numpy, which is a highly optimized library for numerical operations with a MATLAB-style syntax. All the OpenCV array structures are converted to and from Numpy arrays. This also makes it easier to integrate with other libraries that use Numpy such as SciPy and Matplotlib.

# Installation
```
pip install opencv-python
```

## Read
- `openCV.imread(imagePath)` - load the image from the specified path
- `openCV.imshow(frameName, image)` - display an image in a window
- `openCV.imwrite(imagePath)` - save image in the specified path
- `openCV.waitKey(0)` -  allows users to display a window for given milliseconds or until any key is pressed. If the parameter value is 0, you have to press any key from your keyboard to destroy the window, untill it will keep open. If the parameter value is other value instead of 0, it will automatically destroy the window after that amount of milliseconds. It return value is the key that was pressed.
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
- `255*np.ones((512, 512, 3))` - creates a 3-dimensional with 512 rows, 512 columns and 3 depth or color channels. It means each of the value of 512*512 array have another array which contains a list of 3 value represnt rgb color code. It is used to create white image.

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
- `thickness=-1` or `thickness=openCV.FILLED` - filled the shape with color
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

## Draw Rectangle
- `top_left` - specify the position of top left corner of the rectangle
- `bottom_right` - specify the position of bottom right corner of the rectangle

```
import cv2 as openCV
import numpy as np

image = 255 * np.ones((512, 512, 3), dtype=np.uint8)

top_left = (100, 100)
bottom_right = (400, 400)
color = (255, 0, 0)
thickness = 2

openCV.rectangle(image, top_left, bottom_right, color, thickness)

openCV.imshow('Line Image', image)
openCV.waitKey(0)
openCV.destroyAllWindows()
```

![Rectangle](/images/drawRectangle.jpg)

## Draw Ellipse
- `center_coordinates` - Specifies the center of the ellipse.
- `axes_length` - Specifies the length of horizontal & vertical axes
- `angle` - Specifies the rotation angle of the ellipse (in degrees) from horizontal line.
- `startAngle` - Specifies the angle (in degrees) at which the ellipse arc starts. It defines the beginning of the arc.
- `endAngle` - Specifies the angle (in degrees) at which the ellipse arc ends. It defines the termination point of the arc.
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
<img align="right" width="49%" height="auto" src="./images/drawEllipseAngle.jpg" />
<img  width="48%" height="auto" src="./images/drawEllipse.jpg" />

## Draw Polygon
- `isClosed` - A boolean flag indicating whether the last point should be connected to the first point to form a closed loop.
- `pts` - it ontains the coordinates of the vertices of the polygon. Each row represents a vertex, and the polygon will be formed by connecting these vertices in the order they appear in the array.
```
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

pts = pts.reshape((-1, 1, 2))
isClosed = True
color = (255, 0, 0)
thickness = 2

openCV.polylines(image, [pts], isClosed, color, thickness)

openCV.imshow('Line Image', image)
openCV.waitKey(0)
openCV.destroyAllWindows()
```
![Polygon](/images/drawPolygon.jpg)

## Draw Text
- `position` - The coordinates (x, y) where the text should be positioned on the image.
- `fontFamily` - The font style to be used for the text. 
- `fontScale` - The scale factor that multiplies the font size.
```
import cv2 as openCV
import numpy as np

image = 255 * np.ones((512, 512, 3), dtype=np.uint8)

text = 'Hello, OpenCV!'
position = (150, 250)
fontFamily = openCV.FONT_HERSHEY_SIMPLEX
fontScale = 1
color = (255, 0, 0)
thickness = 2

openCV.putText(image, text, position, fontFamily, fontScale, color, thickness)

openCV.imshow('Line Image', image)
openCV.waitKey(0)
openCV.destroyAllWindows()
```
![Text](/images/drawText.jpg)

## Resizing
- `None` - It specifies that you're not providing explicit target dimensions for the resized image. When None is provided, OpenCV calculates the size of the output image based on the specified scaling factors.
- `camera.set(property_identifier, value)` - is used to change the resolution of a live video stream. It doesn't work with images or video, only with live video stream.
```
import cv2 as openCV
import numpy as np

imagePath="images/img1.png"
image = openCV.imread(imagePath)

new_width = 400
new_height = 300
resized_image = openCV.resize(image, (new_width, new_height))

scale_factor = 0.5
scaled_image = openCV.resize(image, None, fx=scale_factor, fy=scale_factor)

openCV.imshow('Original Image', image)
openCV.imshow('Resized Image', resized_image)
openCV.imshow('Scaled Image', scaled_image)

openCV.waitKey(0)
openCV.destroyAllWindows()
```

## Image Property
- `shape` - return a list containing (height, width, channels), If an image is grayscale, the tuple returned contains only the number of rows and columns, so it is a good method to check whether the loaded image is grayscale or color.
- `size` - returns the total number of pixel in the image array, which is the product of its width, height, and number of channels.
- `ndim` - returns the number of dimensions of the image array. For example, grayscale images have 2 dimensions (height and width), while color images have 3 dimensions (height, width, and channels). 
- `min()` and `max()` - return the minimum and maximum pixel values in the image array, respectively.
- `mean()` and `std()` - return the mean and standard deviation of pixel values in the image array, respectively.
- `dtype` - return datatype of an image. It is very important while debugging because a large number of errors are caused by invalid datatype.

## Translation

- `openCV.warpAffine()` - is used to perform the image translation which takes the input image, the translation matrix, and the output image size (width, height) as parameters. The function applies the specified transformation to the input image, resulting in the translated image based on translation matrix.

- `openCV.getRotationMatrix2D()` - calculates the transformation matrix needed to perform the rotation. It takes the rotation center, the rotation angle, and the scale factor as parameters.
```
[
  [  0.70710678   0.70710678 -56.10973978]
  [ -0.70710678   0.70710678 282.53910524]
]
```
- `np.float32()` - It generate a matrix which represents the transformation to be applied to the image. It defines how much the image should be shifted in the x and y directions.
```
[
  [  1.   0. 100.]
  [  0.   1.  50.]
]
```
- `openCV.getAffineTransform()` - takes the `source points` and `destination points` as parameters and computes the transformation matrix needed to map the source points to the destination points. Source and destination set contains three points, where each point represents a vertex of a triangle. These triangles define the affine transformation.
```
[
  [  1.   0. 100.]
  [  0.   1.  50.]
]
```

Affine transformations are operations that include translation, rotation, scaling, and shearing. It represented using transformation matrices. For a 2D affine transformation, the transformation matrix is a 2x3 matrix, where each column represents the transformation applied to the x and y coordinates, and the last column represents translation.

## Splitting & Merging

__Concatenation__ involves arranging multiple images side by side or on top of each other to create a larger image. __Merging__ involves combining the pixel values of two or more images to create a new image. __Splitting__ involves separating the color chanels.

- `openCV.split(image)` - splits the input image into its individual channels: blue, green, red. The result is three separate arrays representing the intensity of each color channel across the entire image. Each pixel of given image have 3 different color value, this method separate it and blue value return in blue part and so on. Splitting an image into its individual color channels allows you to analyze or manipulate each color component separately. For example, you can perform operations such as adjusting the brightness or contrast of a specific color channel, enhancing certain colors, or creating special effects.

- `openCV.merge((b, g, r))` - merges the individual color channels. Merging the individual color channels back together is often necessary after performing operations on individual channels, such as color manipulation or filtering, to reconstruct the complete image with the desired modifications.

- `openCV.hconcat()` - is used to concatenate the images horizontally by passing a list of images to concatenate.
- `openCV.vconcat()` - is used to concatenate the images vertically by passing a list of images to concatenate.

### Uses:
__Color Correction:__ Correcting color balance in an image might need to adjust the intensity of each color chanel independently. For example, if an image appears too blue due to incorrect white balance, you can reduce the intensity of the blue channel to balance the colors.

__Image Enhancement:__ if you want to enhance the contrast of the sky in a landscape photo, you might adjust the intensity of the blue channel to make the sky more vibrant without affecting other parts of the image.

__Feature Extraction:__ Object detection rely on specific color information. For example, in medical imaging, certain tissues or structures might be more distinguishable in a particular color channel.

__Water Detection:__ Water bodies can be detected by analyzing the intensity of the blue channel. Water usually absorbs more red and green light, while reflecting more blue light, making it stand out in the blue channel.

__Night Vision:__ Green color channels are often emphasized because the human eye is most sensitive to green light. By merging a grayscale image with an enhanced green channel, you can improve visibility in low-light conditions while preserving important details.

## Arithmatic Operations

__Brightness:__ Adding a `constant` value to every pixel in an image increases its brightness, while subtracting decreases it. This operation is often used for adjusting the exposure of images.

__Contrast:__ Multiplying every pixel in an image by a `constant` value increases its contrast, while dividing decreases it. Contrast adjustment helps in enhancing the visual quality of images.

__Motion Detection:__ Subtracting one image from another can highlight the differences between them. This operation is useful in applications such as motion detection, where consecutive frames of a video are subtracted to identify moving objects.

__Masking:__ Multiplying an image by a` binary mask` (where pixel values are either 0 or 1) selectively applies the mask to the image. This technique is commonly used for image segmentation and region-of-interest extraction.

## Grayscale Image
Grayscale Image only contain a single channel representing the intensity of light at each pixel, without any color information. It is achieved by taking a `weighted sum of the Red, Green, and Blue channels` of the original image. The weights are typically chosen to match the perceived brightness of the different color channels. Finally, the resulting intensity value is assigned to each pixel in the grayscale image.

A grayscale image is a type of digital image in which each pixel represents a single intensity value that denotes the light intensity, ranging from black to white. Unlike color images, which have multiple color channels (such as RGB - Red, Green, Blue), grayscale images contain only one channel.

1. __Single Intensity Channel:__ Each pixel in a grayscale image has a single value representing the intensity of light. The value typically ranges from 0 to 255 in 8-bit images, where:

    - `0` represents black (no light).
    - `255` represents white (maximum light intensity).
    - Values between 0 and 255 represent varying shades of gray.
2. __Simplified Data Structure:__ Because grayscale images have only one channel, they require less memory and computational power compared to color images. This makes them suitable for many image processing tasks where color information is not crucial.
3. __Applications:__ Grayscale images are widely used in image processing, computer vision, and machine learning for tasks such as edge detection, pattern recognition, and thresholding.

__Grayscale Image:__
```
image = np.zeros((500, 500), dtype=np.uint8)
cv2.circle(image, (250, 250), 100, 255, -1)
```
__Color Image:__
```
image = np.zeros((500, 500, 3), dtype=np.uint8)
cv2.circle(image, (250, 250), 100, (255, 0, 0), -1)
```
__Convert Color Image to Grayscale Image:__
```
gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
```

## HSV Image
An HSV color model is the most accurate color model as long as the way humans perceive colors. How humans perceive colors is not like how RGB or CMYK make colors. They are just primary colors fused to create the spectrum.

- `Hue` - It represents the color itself. It is typically represented as an angle around a color wheel, ranging from 0 to 360 degrees, covering the spectrum of colors.
- `Saturation` - It represents the purity of the color. Higher saturation values indicate more vibrant colors, while lower values approach shades of gray.
- `Value` - It represents the brightness or intensity of the color. Higher values correspond to brighter colors, while lower values approach black.

Pixel value:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[240 221 210]<br>
HSV value of 240: [109  32 240]

|Angle|Color|
|---|---|
|0-60|Red|
|60-120|Yellow|
|120-180|Green|
|180-240|Cyan|
|240-300|Blue|
|300-360|Magenta|


## Blur Image
A blurred image is an image in which the sharpness or details have been reduced intentionally through a process known as blurring. Blurring is a common technique in image processing used to reduce noise, smooth out irregularities, or obscure details in an image.

```
   Original   =>    Blurred
[243 224 213] => [240 221 210]
[243 225 214] => [244 225 214]
[244 228 218] => [245 228 219]
```

## Haris Corner Detection
Harris corner detection method is used detecting interest points or corners in an image. It's particularly robust to changes in lighting conditions and image noise

- __Corner Detection Principle:__ Corners are points in an image where there are significant variations in intensity in `multiple directions`. These variations can be detected by examining the `gradient` of the image intensity.
- __Gradient Calculation:__ Harris corner detection begins by computing the gradient of the image intensity using techniques such as `Sobel`. This step provides information about the direction and magnitude of intensity changes at each pixel.
- __Structure Tensor Calculation:__ A structure tensor is computed for each pixel in the image. The structure tensor summarizes the gradient information in a local neighborhood around each pixel and describes the local structure of the image.
- __Corner Response Function:__ The Harris corner detector defines a corner response function, which evaluates how likely each pixel is to be a corner based on the eigenvalues of the structure tensor. Pixels with high corner responses are considered corner candidates.
- __Non-maximum Suppression:__ To remove redundant corner candidates and select only the most prominent corners, non-maximum suppression is applied. This process involves comparing the corner response values of neighboring pixels and retaining only the local maxima.
- __Thresholding:__ A thresholding step is often applied to the corner response values to discard weak corners and retain only the strongest ones.

- `block_size` - represents the size of the neighborhood considered for corner detection. It is the size of the kernel for the Sobel operator.
- `ksize` - Aperture parameter of the Sobel derivative used for corner detection.
- `k` - Harris detector free parameter in the equation (usually in the range of 0.04 to 0.06).
- `openCV.cornerHarris()` - returns a response map containing the corner response values for each pixel.
- `threshold = 0.01 * dst.max()` - applies thresholding to the corner response map to identify prominent corners. It calculates a threshold value as 1% of the maximum response value.
- `image[dst > threshold] = [0, 0, 255]` - it marks the detected corners on the original image by setting the color of the pixels with a corner response above the threshold to red ([0, 0, 255]).

## Contours Detection

Contours are curves joining continuous points along a boundary that have the **same color** or intensity