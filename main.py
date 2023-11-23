# MORPHOLOGICAL OPERATION  :

# Morphology is a broad set of image processing operations that
# process binary images based on structuring element or kernel which
# decides the nature of operation.

# In a morphological operation, each pixel in the image i
# adjusted based on the value of other pixels in its
# neighborhood.

# 1 Dilation  : - increase
# 2. Erosion : - decrease
# 3. Opening : - out  side noise removal
# 4. closing :- inside noise removal
# 5. Gradient :- find outline
# 6.Top Hat
# 7. Black Hat

# THRESHOLDING : Thresholding is easiest form of Image Segmentation based on
# Intensity Value of Pixels. 
# Thresholding is one of the segmentation techniques that generates a binary image

import cv2 
import numpy as np
import matplotlib.pyplot as plt 

img = cv2.imread("Task2.jpeg",0)

# ret = optimum thresholding value, th = array or thresolded image --->>
ret, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

# Define a kernel 
kernel = np.ones((3,3), np.uint8)

# Perform dilation
dilation = cv2.dilate(th, kernel, iterations=1)
cv2.imwrite('dilation_result.jpg', dilation)

# Perform erosion
erosion = cv2.erode(th, kernel, iterations=1)
cv2.imwrite('erosion_result.jpg', erosion)

opening = cv2.morphologyEx(th, cv2.MORPH_OPEN, kernel)
cv2.imwrite('opening_result.jpg', opening)


