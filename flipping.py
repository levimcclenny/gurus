# import the necessary packages
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help = "Path to the image")
args = vars(ap.parse_args())
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
# flip the image horizontally
flipped = cv2.flip(image, 1)
(h, w) = image.shape[:2]
(cX, cY) = (w / 2, h / 2)
M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
rotated = cv2.warpAffine(flipped, M, (w, h))

flipped = cv2.flip(rotated, 0)


cv2.imshow("Flipped Horizontally", flipped)
(b, g, r) = flipped[189, 441]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
# # flip the image vertically
# flipped = cv2.flip(image, 0)
# cv2.imshow("Flipped Vertically", flipped)
# # flip the image along both axes
# flipped = cv2.flip(image, -1)
# cv2.imshow("Flipped Horizontally & Vertically", flipped)
# cv2.waitKey(0)