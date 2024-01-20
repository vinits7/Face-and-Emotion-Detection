# Face detection, recognition and Tracking

*For detatailed information - kindly refer to project report.pdf*

In this project, I have worked towards the following two targets:

1. To create an Arduino model that can detect and track faces.
2. To build an attendance system based on face recognition technology

Human faces are identified and localized using facial detection, which ignores any backdrop objects such as curtains, windows, trees, and so on. OpenCV employs a Harr cascade of classifiers, in which each frame of video is sent through a series of classifiers; if the frame passes through all of them, the face is present; otherwise, the frame is thrown from the classifier, indicating that the face was not detected.
When an image is detected, OpenCV returns the cartesian coordinates, as well as the height and width. x+width/2 and y+height/2 can be used to calculate the image's center coordinates from these coordinates.
When the face is detected, these coordinates are sent to the Arduino UNO using the pyserial library. The camera is attached to one of the servos connected to the Arduino, which provides a pan/tilt mechanism. When the face's coordinates are off from the center, the servo will align by 2 degrees (increment or decrement) to bring it closer to the screen's center.

A facial recognition software captures and compares patterns on a person's face, as well as analyses the details, in order to identify and verify the person. Despite the complexity of the underlying mechanism, the entire technique may be boiled down into three steps:
1. Face Detection: Locating human faces in real-time is an important step.
2. Data Transformation: The analogue facial data is converted into a set of data or vectors based on a person's facial traits once it is taken.
3. Face Match: The system verifies the data above by comparing it to the data in the database.
