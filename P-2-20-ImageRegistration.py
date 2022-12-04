import cv2 as cv
import numpy as np

# Open the image files.
img1_color = cv.imread("Ch2-images/book1_small_small.jpg") # Image to be aligned.
img2_color = cv.imread("Ch2-images/book2_small_small.jpg") # Reference image.

# Convert to grayscale.
img1 = cv.cvtColor(img1_color, cv.COLOR_BGR2GRAY)
img2 = cv.cvtColor(img2_color, cv.COLOR_BGR2GRAY)

height, width = img2.shape

# Create ORB detector with 5000 features.
orb_detector = cv.ORB_create(5000)

# Find keypoints and descriptors.
# The first arg is the image, second arg is the mask
# (which is not reqiured in this case).
kp1, d1 = orb_detector.detectAndCompute(img1, None)
kp2, d2 = orb_detector.detectAndCompute(img2, None)

# Match features between the two images.
# We create a Brute Force matcher with
# Hamming distance as measurement mode.
matcher = cv.BFMatcher(cv.NORM_HAMMING, crossCheck = True)

# Match the two sets of descriptors.
matches = matcher.match(d1, d2)

# Sort matches on the basis of their Hamming distance.
matches.sort(key = lambda x: x.distance)

# Take the top 90 % matches forward.
matches = matches[:int(len(matches)*90)]
no_of_matches = len(matches)

# Define empty matrices of shape no_of_matches * 2.
p1 = np.zeros((no_of_matches, 2))
p2 = np.zeros((no_of_matches, 2))

for i in range(len(matches)):
	p1[i, :] = kp1[matches[i].queryIdx].pt
	p2[i, :] = kp2[matches[i].trainIdx].pt

# Find the homography matrix.
homography, mask = cv.findHomography(p1, p2, cv.RANSAC)

# Use this matrix to transform the
# colored image wrt the reference image.
transformed_img = cv.warpPerspective(img1_color,
					homography, (width, height))

# Save the output.
cv.imwrite('Ch2-images/output.jpg', transformed_img)
cv.imshow("test",transformed_img)
cv.waitKey(0)
