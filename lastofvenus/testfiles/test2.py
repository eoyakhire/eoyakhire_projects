import cv2
import numpy as np

def analyze_skin_color(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to the YCbCr color space
    ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

    # Extract the Y, Cr, and Cb channels
    y, cr, cb = cv2.split(ycbcr_image)

    # Calculate mean values for each channel
    y_mean = np.mean(y)
    cr_mean = np.mean(cr)
    cb_mean = np.mean(cb)

    # Output the mean values as a representation of skin color
    return y_mean, cr_mean, cb_mean

# Replace 'input_image.jpg' with the path to your input image
input_image_path = 'images/anime2.jpg'

# Analyze skin color and get mean values
y_mean, cr_mean, cb_mean = analyze_skin_color(input_image_path)

# Print the results
print(f'Mean Y: {y_mean}')
print(f'Mean Cr: {cr_mean}')
print(f'Mean Cb: {cb_mean}')