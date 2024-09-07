import cv2 #name for opencv

# Load the image
image = cv2.imread('img1.jpg')

# Check if the image was loaded successfully
if image is None:
    print("Error: Could not open or find the image.")
else:
    #to display image
    cv2.imshow('Image', image)

    
    cv2.waitKey(0)
    
    cv2.destroyAllWindows() #destry the image
