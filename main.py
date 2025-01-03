import cv2 as cv
import numpy as np
import matplotlib

### Read Image in black and white
###
### Arg: filepath to the image being turned into black and white

def read_image_bw(filepath):
    
    # Turn image to black and white and show the image
    img = cv.imread(filepath, cv.IMREAD_GRAYSCALE)
    cv.imshow("Image Black n White", img)

    # Wait for user to close out image tab
    cv.waitKey(0)
    cv.destroyAllWindows()

# Local image and function call
filepath = "C:\\Users\\sprab\\Downloads\\Lebron_James.jpg"
read_image_bw(filepath)