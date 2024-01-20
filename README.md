# Face detection, recognition and Tracking

*For detatailed information - kindly refer to project report.pdf*

In this project, I have worked towards the following two targets:

1. To create an Arduino model that can detect and track faces.
2. To build an attendance system based on face recognition technology

Face Detection and Tracking with Arduino Uno:

This GitHub repository contains the implementation of a Face Detection and Tracking system using Arduino Uno. Additionally, it includes a Face Recognition-based Attendance System. The project utilizes computer vision techniques and Arduino hardware to detect, track, and recognize faces in real-time.

Features:

1. Face Detection and Tracking with Arduino Uno
Utilizes OpenCV's Harr cascade classifiers for face detection.
Implements a dual servo mechanism connected to Arduino Uno for tracking the detected face.
Components used: Arduino Uno, USB Camera, Servo Motors (SG90), Breadboard, Jumper Wires.

2. Face Recognition-based Attendance System
Uses a Python script with OpenCV for facial recognition.
Recognizes faces by comparing them with a database of stored student images.
Records attendance in a CSV file with timestamps.
Includes a simple GUI using tkinter for capturing attendance and viewing attendance records.
Components used: Python, OpenCV, tkinter.

Arduino Setup

1.Components Connection
Connect the Arduino Uno to two servo motors for pan/tilt mechanism.
Attach the USB camera to capture video input.

2.Code Installation
Install necessary libraries using pip: pip install pyserial opencv-python
Download the pre-trained Haarcascade XML file for face detection.
Update the COM port in the Arduino code (line 9) before execution.

Python Setup
1. Installation
Install required libraries: pip install opencv-python face-recognition

2. Student Database
Place student images in the "student_images" folder with filenames as their full names.

3. Attendance Sheet
Create an "at" folder with a CSV file for storing attendance records.

Usage

1.Arduino Code
Upload the Arduino code to the Arduino Uno board.

2. Python Code
Run the Python script (temp2.py) for face recognition and attendance.

3. GUI
Execute UI.py for a simple GUI to capture attendance and view records.

Scope for Improvement
1. Add features for automated database updates and handling multiple lectures in a day.
2. Implement a cloud-based module for real-time student additions.
3. Enhance UI for better user experience.
4. Incorporate analytics tools for attendance percentages.

Disclaimer
This project was developed by Vinit Shah. Any inquiries or contributions should be directed to Vinit Shah at vinshah333@gmail.com

References
[Arduino Uno - Getting Started Guide](https://www.rs-online.com/designspark/what-is-arduino-uno-a-getting-started-guide)

[Face Detection Technology](https://www.techtarget.com/searchenterpriseai/definition/face-detection)

[Arduino Projects](https://projecthub.arduino.cc/)

# Face Recognition System

## Abstract
Facial recognition systems, utilizing Haar Cascade and Convolutional Neural Network (CNN) algorithms, have gained popularity for security and personal device access. This project focuses on real-time face detection, emotion analysis, and eye tracking using OpenCV and Python.

## Objective
Develop a model for real-time face detection, emotion analysis, and eye tracking using Haar Cascade and CNN algorithms.

## Proposed Design
Utilize Python, Haar Cascade, and CNN algorithms for accurate face and emotion identification. Haar Cascade detects faces, CNN identifies eyes and emotions. Integration provides applications in facial recognition, video surveillance, and emotion detection for human-robot interaction.

## Methodology

### Haar Cascade Algorithm:
1. **Collect images:**
   Gather positive (faces) and negative images for classifier training.

2. **Train the classifier:**
   Use AdaBoost for feature selection, creating Haar features capturing image contrasts.

3. **Cascade of classifiers:**
   Apply a series of classifiers with increasing detection rates and lower false positives.

4. **Post-processing:**
   Enhance accuracy through post-processing, filtering false positives.

### CNN Algorithm for Emotion Detection:
1. **Data Preparation:**
   Collect labeled facial images for emotion training.

2. **CNN Architecture Design:**
   Design CNN architecture for effective feature extraction.

3. **Training:**
   Train the CNN model on the dataset, adjusting weights to minimize prediction errors.

4. **Testing and Evaluation:**
   Evaluate performance on a test dataset using metrics like accuracy and precision.

5. **Deployment:**
   Deploy the trained CNN for emotion prediction on new images.

## Implementation
- **Face Detection:**
  Use Haar Cascade classifier in Python with OpenCV for face detection in images or videos.

- **Eye Detection:**
  Implement Haar Cascade classifier for eye detection in Python using OpenCV.

- **Emotion Detection:**
  Use Convolutional Neural Network (CNN) in Python with TensorFlow and Keras for emotion detection.

## Results and Conclusion
The model accurately recognizes faces and basic emotions in real-time, demonstrating potential applications in various fields.

## Social Impact
While face and emotion recognition systems offer significant benefits, careful consideration of ethical and social implications is crucial to address concerns such as privacy and accuracy.
