import cv2
import imutils


# HAAR Cascade Classifiers
face_cascade = cv2.CascadeClassifier('haar_cascade\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haar_cascade\\haarcascade_eye.xml')

# Get Image Location/File
evidence = cv2.imread('evidence\\Filter\\IMG7.jpg')

# Process and Convert the Image to Grey
grey = cv2.cvtColor(evidence, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey, 1.3, 5)

# evidence = imutils.resize(evidence, width=500)

# Detect Face and Eyes (x, y, width, height)
for (x, y, w, h) in faces:
    cv2.rectangle(evidence, (x, y), (x + w, y + h), (255, 0, 0), 2)

    roi_gray = grey[y:y+h, x:x+w]
    roi_color = evidence[y:y+h, x:x+w]

    eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
    for (ex, ey, ew, eh) in eyes :
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# Display the Image
cv2.imshow('Face and Eye Detection', evidence )


# Waits for Key Press to Terminate Window
cv2.waitKey(0)
cv2.destroyAllWindows()