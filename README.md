# Automated Detection of Fake Digital Images

# ![image](https://user-images.githubusercontent.com/81099987/170871559-2748b2ed-6664-44d1-98fc-aa07fbdd043f.png)

This is my product submission for the partial requirement of my dissertation worth 30%.

# Prerequisites and Installation

Python 3, OpenCV, Cmake, Dlib, imutils, numPy, QT Designer

# About HAAR Cascade
The Haar-Cascade algorithm is a machine learning object detection algorithm, used to identify specific objects based upon the features that are found in an image or many images played together (i.e., video or live capture).

> Classifiers:

> Frontal_Face: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

> Eye: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_eye.xml

 HAAR Execution
> Enter Path Where File Exists.
>
> Hard-code the image for detection
> 
> Run haar.py.


# About Dlib 
Dlib can detect the 68 facial landmarks including the jawline and eyebrows. It estimates the location of 68 coordinates (x, y) and plots the points on an image.

> Shape Predictor:

> https://github.com/tzutalin/dlib-android/blob/master/data/shape_predictor_68_face_landmarks.dat

 Dlib Execution

> Enter Path Where File Exists.
> 
> Ensure .dat File Is In The Same Location As The .py File.
> 
> Run python landmark.py --shape-predictor shape_predictor_68_face_landmarks.dat --image evidence/Filter/IMG2.jpg

# About RGB
The colour of a single pixel is represented as 3 numbers between 0 and 255, corresponding to Red, Green, and Blue (RGB).

 RGB Execution 
> Print Coordinates From HAAR Eye Detection.
> >
> Enter Path Where File Exists.
> >
> Edit Code To Correlate With Eye Coordinates
> 
> Run rgb.py

# GUI
The GUI has been created using QT Designer, all features are implemented however the GUI is not functional.

> To convert QT Designer file to .py run the following commmand:
> 
> pyuic5 -x tool.ui -o tool.py




