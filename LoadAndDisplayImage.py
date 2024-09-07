import cv2

# Load the image
image = cv2.imread('img1.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
else:
    # Display the image in a window
    cv2.imshow('Image', image)

    # Wait indefinitely until a key is pressed
    cv2.waitKey(0)

    # Destroy all OpenCV windows
    cv2.destroyAllWindows()
