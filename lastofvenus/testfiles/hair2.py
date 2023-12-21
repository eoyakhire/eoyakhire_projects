import cv2
import numpy as np

def calculate_hair_color_difference(image1_path, image2_path):
    # Load the images
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    # Convert the images to the HSV color space
    hsv_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2HSV)
    hsv_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for hair color in HSV
    lower_bound = np.array([0, 10, 10], dtype=np.uint8)
    upper_bound = np.array([30, 255, 255], dtype=np.uint8)

    # Create masks to extract hair color
    mask1 = cv2.inRange(hsv_image1, lower_bound, upper_bound)
    mask2 = cv2.inRange(hsv_image2, lower_bound, upper_bound)

    # Extract hair color from the original images
    hair_color1 = cv2.bitwise_and(image1, image1, mask=mask1)
    hair_color2 = cv2.bitwise_and(image2, image2, mask=mask2)

    # Calculate the mean color of the extracted hair
    mean_color1 = np.mean(hair_color1, axis=(0, 1))
    mean_color2 = np.mean(hair_color2, axis=(0, 1))

    # Calculate the absolute difference between mean hair colors
    mean_color_diff = np.abs(mean_color1 - mean_color2)

    return mean_color_diff

# Example usage
image_path1 = 'images/anime.png'
image_path2 = 'images/anime2.jpg'

hair_color_difference = calculate_hair_color_difference(image_path1, image_path2)
print(f'The difference in hair color is: {hair_color_difference}') 