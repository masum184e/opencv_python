import cv2 as openCV
    
camera = openCV.VideoCapture(0)

if not camera.isOpened():
    print("Error: Failed to open camera.")

isReading, frame = camera.read()

if not isReading:
    print("Error: Failed to capture frame.")

openCV.imshow('Captured Image', frame)

image_path = 'images/captured_image.jpg'
openCV.imwrite(image_path, frame)
print(f"Image saved as {image_path}")

camera.release()
openCV.destroyAllWindows()