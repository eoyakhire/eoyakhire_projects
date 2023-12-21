import face_recognition
import cv2
import numpy as np

class Image:
    def __init__(self, image_path, y, cr, cb, total, img=None):
        self.image_path = image_path
        self.y = y
        self.cr = cr
        self.cb = cb
        self.total = total
        self.img = img

    def calculate_diff(self):
        if self.total is not None and self.img and self.img.total is not None:
            return np.abs(self.total - self.img.total)
        else:
            return None

    @classmethod
    def from_path(cls, image_path, img=None):
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        
        # Initialize variables outside the loop
        total = 0
        y, cr, cb = 0, 0, 0
        
        for face_location in face_locations:
            top, right, bottom, left = face_location
            face_image = image[top:bottom, left:right]

            # Convert the face image to YCbCr color space
            ycbcr_face = cv2.cvtColor(face_image, cv2.COLOR_BGR2YCrCb)
            y, cr, cb = cv2.split(ycbcr_face)
            total += np.mean(y) + np.mean(cr) + np.mean(cb)
                    
        # image = cv2.imread(image_path)
        # ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        # y, cr, cb = cv2.split(ycbcr_image)
        # total = np.mean(y) + np.mean(cr) + np.mean(cb)
        return cls(image_path, np.mean(y), np.mean(cr), np.mean(cb), total, img=img)

# Creates instances of the Image class for the user's image and the 
og_image = Image.from_path('images/emile2.png')
image1 = Image.from_path('images/anime.png', img=og_image)
image2 = Image.from_path('images/anime2.jpg', img=og_image)

# Calculates differences of the mean between each image and the inputed image of the user 
image1_difference = image1.calculate_diff()
image2_difference = image2.calculate_diff()

print("image 1 difference to og image:", image1_difference)
print("image 2 difference to og image:", image2_difference)

# Finding the image with the minimum difference in the anime database (array of images)
images = [image1, image2]
min_difference_image = min(images, key=lambda img: img.calculate_diff())

# Displays the image with the minimum difference, which means that the two images must be close in color and thus must have similar skintones
print("Image with the minimum difference to the original image:", min_difference_image.image_path)
output_image = cv2.imread(min_difference_image.image_path)

# Displays the corresponding animated image 
cv2.imshow('Anime Image', output_image) 

# Closes the window that displays the image when the user presses 0 on their keyboard 
cv2.waitKey(0) 
cv2.destroyAllWindows() # Closes windows once the command is excuted 

        # image = cv2.imread(image_path)
        # ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)
        # y, cr, cb = cv2.split(ycbcr_image)
        # total = np.mean(y) + np.mean(cr) + np.mean(cb)