# python landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image evidence/Filter/IMG2.jpg

import cv2
import imutils
import dlib
import argparse
import numpy as np
from imutils import face_utils

# Construct the argument parser and parse the arguments
# Used for running the .py file noted at line 1
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True)
ap.add_argument("-i", "--image", required=True)
args = vars(ap.parse_args())

# Initialise dlib's face detector (HOG-based)
# Create the facial landmark predictor
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])

# Load the evidence
evidence = cv2.imread(args["image"])

# Resize the evidence
evidence = imutils.resize(evidence, width=500)

# Convert the evidence to grayscale
gray = cv2.cvtColor(evidence, cv2.COLOR_BGR2GRAY)

# Use dlib face dectector in grayscale
gray_face = detector(gray, 1)

# Loop (for) over the face detections
for (i, rect) in enumerate(gray_face):
    # Determine the facial landmarks for the face region
    face = predictor(gray, rect)
    # Convert the facial landmark (x, y) to a NumPy array
    face = face_utils.shape_to_np(face)

    # Loop (for) over the (x, y) for the facial landmarks
    # Draw them on the evidence file
    for (x, y) in face:
        # Facial landmarks plotted in green, size 1
        cv2.circle(evidence, (x, y), 1, (0, 255, 0), 1)

# Show the plotted facial landmarks
cv2.imshow("Facial Landmark Detection", evidence)
cv2.waitKey(0)