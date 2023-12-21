import face_recognition  # Facial recognition library that detects faces in photos 
import cv2 # Library that can load/dispplay images and read the color channels 
import numpy as np
from flask import Flask, render_template, request, redirect, url_for, send_from_directory # Used for backend code to help make the code a web application for user's to actually use
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

class Image:
    def __init__(self, image_path, y, cr, cb, total, hue, hue_threshold=30, img=None):

        # Initalizes the variables 
        self.image_path = image_path
        self.y = y
        self.cr = cr
        self.cb = cb
        self.total = total
        self.hue = hue 
        self.hue_threshold = hue_threshold
        self.img = img

    # Function that calculates the difference in color betweent the user's image and the images in the file 
    def calculate_diff(self):
        if self.total is not None and self.img and self.img.total is not None:
            return np.abs(self.total - self.img.total)
        else:
            return None
    
    def calculate_hair_color_similarity(self, hair_image):

        # Convert the hair image to the HSV color space
        hsv_hair_image = cv2.cvtColor(hair_image, cv2.COLOR_BGR2HSV)

        # Calculate the absolute difference in hue
        #if self.hue is not None and self.img and self.img.hue is not None: 
       #     return np.abs(self.hue - self.img.hue)
       # else: 
        #    return None

        # Extract the hue channel
        hue_hair = hsv_hair_image[:, :, 0]

        # Resize the hue channel to a fixed size for comparison
        resized_hue = cv2.resize(hue_hair, (1024, 1024))

        # Calculate the absolute difference in hue
        if self.hue is not None:
            return np.abs(self.hue - resized_hue)
        else:
            return None

    @classmethod
    def from_path(cls, image_path, img=None):
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)
        
        # Initializes variables outside the loop
        total = 0
        y, cr, cb = 0, 0, 0
        hue_values = []  # To store hue values for later calculation

        
        # Detects a face from a given image 
        for face_location in face_locations:
            top, right, bottom, left = face_location
            face_image = image[top:bottom, left:right]

            # Converts the face image to YCbCr color space
            ycbcr_face = cv2.cvtColor(face_image, cv2.COLOR_BGR2YCrCb)
            y, cr, cb = cv2.split(ycbcr_face)
            total += np.mean(y) + np.mean(cr) + np.mean(cb) # Calculates the total average 

            # Calculate hair-related features
            hsv_face = cv2.cvtColor(face_image, cv2.COLOR_BGR2HSV)
            hue_values.append(np.mean(hsv_face[:, :, 0]))

        # Calculate the mean hue value for the entire image
        hue = np.mean(hue_values)

        # hair_image = cv2.imread(image_path) <--last time

        # Convert the images to the HSV color space
        # hsv_image = cv2.cvtColor(hair_image, cv2.COLOR_BGR2HSV)

        # Extract the hue channel
        # hue = hsv_image[:,:,0]
        # Resize the hue channel to a common size (e.g., 1024x1024)
        
        # resized_hue = cv2.resize(hair_image[:, :, 0], (1024, 1024)) <--- last time

        # Returns the values 
        return cls(image_path, np.mean(y), np.mean(cr), np.mean(cb), total, hue, hue_threshold=30, img=img)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # Obtains each of the image files from my folder and from the user 
        og_image = Image.from_path(filepath)
        image1 = Image.from_path('images/anime.png', img=og_image)
        image2 = Image.from_path('images/anime2.jpg', img=og_image)
        image3 = Image.from_path('images/anime3.jpg', img=og_image)
        image4 = Image.from_path('images/anime4.jpg', img=og_image)
        image5 = Image.from_path('images/anime5.jpg', img=og_image)
        image6 = Image.from_path('images/anime6.jpg', img=og_image)
        image7 = Image.from_path('images/anime7.jpg', img=og_image)
        image8 = Image.from_path('images/anime8.jpg', img=og_image)
        image9 = Image.from_path('images/anime9.jpg', img=og_image)
        image10 = Image.from_path('images/anime10.jpg', img=og_image)
        image11 = Image.from_path('images/anime11.jpg', img=og_image)
        image12 = Image.from_path('images/anime12.jpg', img=og_image)
        image13 = Image.from_path('images/anime13.jpg', img=og_image)
        image14 = Image.from_path('images/anime14.jpg', img=og_image)
        image15 = Image.from_path('images/anime15.jpg', img=og_image)
        image16 = Image.from_path('images/anime16.jpg', img=og_image)
        image17 = Image.from_path('images/anime17.jpg', img=og_image)
        image18 = Image.from_path('images/anime18.jpg', img=og_image)
        image19 = Image.from_path('images/anime19.jpg', img=og_image)

        # An array of the images 
        images = [image1, image2, image2, image3, image4, image5, image6, image7, image8, image2, image9, image10, image10, image11, image12, image13, image14, image15, image16, image17, image18, image19]
        hair_images = []

        # Loop through the images and calculate differences
        # Calculates differences of the mean between each image and the inputed image of the user 
        for img in images:

            hair_image = cv2.imread(img.image_path)

            img.calculate_hair_color_similarity(hair_image)

            # Apply a threshold for similarity
            if np.mean(img.calculate_hair_color_similarity(hair_image)) < img.hue_threshold: 
                # add the image to another array where all the photos have the same hair color 
                hair_images.append(img)
                print(f"Number of images with similar hair color: {len(hair_images)}")

            if hair_images is not None: 
                for img in hair_images:
                    img.calculate_diff()

            # hair_image = cv2.imread(img.image_path)


        # Finding the image with the minimum difference in skin tone the anime database (array of images)
        # min_difference_image = min(images, key=lambda img: img.calculate_diff())
        min_difference_image = min(hair_images, key=lambda img: img.calculate_diff())

        # Displays the image with the minimum difference, which means that the two images must be close in color and thus must have similar skintones
        output_image = cv2.imread(min_difference_image.image_path)
        cv2.imwrite('uploads/output_image.jpg', output_image)

        return render_template('result.html', input_image=filepath)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
