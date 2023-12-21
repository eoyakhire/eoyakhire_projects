import cv2
import numpy as np

class Image:
    def __init__(self, image_path,  y, cr, cb, total, img=None):
        self.image_path = image_path
        self.y = y
        self.cr = cr
        self.cb = cb
        self.total= total # calculate this another way 
        self.img = img

    # we need to calculate the users image channel total too 
    # need to implement the other function
    # figure out the displaying the path 
    # having the user input an image path

    def calculate_diff(self): 
        if self.img:
                return np.abs(self.total - self.img.total)
        else:
            return None

    def analyze_skin_color(self):
        if self.image_path: 
            # Load the image
            image = cv2.imread(self.image_path)

            # Convert the image to the YCbCr color space
            ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

            # Extract the Y, Cr, and Cb channels
            y, cr, cb = cv2.split(ycbcr_image)

            # Calculate mean values for each channel
            y_mean = np.mean(y)
            cr_mean = np.mean(cr)
            cb_mean = np.mean(cb)
            total_mean = y_mean + cr_mean + cb_mean

            # Output the mean values as a representation of skin color
            return total_mean

            # Replace 'input_image.jpg' with the path to your input image
            #input_image_path = 'images/anime2.jpg'

            # Analyze skin color and get mean values
            # y_mean, cr_mean, cb_mean = analyze_skin_color(input_image_path)
        else: 
            return None  

# Creating instances of the Person class
# og_image = (path, y_mean, cr_mean, cb_mean, total)
og_image = Image('images/emile2.png', 85.44678232621173, 132.83351187154548, 136.13905552455358, 354.4193497223108)
image1 = Image('images/anime.png', 56.157798767089844, 136.92377948760986, 126.64550876617432, 319.72708602087404, img=og_image)
image2 = Image('images/anime2.jpg', 187.38307762145996, 138.63723754882812, 121.60652732849121, 447.6268424987793, img=og_image)

# Calculating salary differences
image1_difference = image1.calculate_diff()
image2_difference = image2.calculate_diff()
og_image_difference = og_image.calculate_diff()


print("image 1 difference to og image:", image1_difference)
print("image 2 difference to og image:", image2_difference)
print("og image difference to og image:", og_image_difference)

# Finding the person with the minimum salary difference
people = [image1, image2]
min_difference_person = min(people, key=lambda person: person.calculate_diff())

# Displaying the person with the minimum salary difference
print("Person with the minimum salary difference to their boss:", min_difference_person.image_path)