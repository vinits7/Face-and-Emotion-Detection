import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('C:\\Users\\VINIT\\Downloads\\detection\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\VINIT\\Downloads\\detection\\haarcascade_eye_tree_eyeglasses.xml')
#smiles_cascade = cv2.CascadeClassifier('C:\\Users\VATSAL ZAVERI\\OneDrive\\Desktop\\strike\\haarcascade_smile.xml')
#mouth_cascade = cv2.CascadeClassifier('C:\\Users\VATSAL ZAVERI\\OneDrive\\Desktop\\strike\\haarcascade_mcs_mouth.xml')

# To capture video from webcam. 
cap = cv2.VideoCapture(0)
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        #smiles = smiles_cascade.detectMultiScale(roi_gray)
        #mouth = mouth_cascade.detectMultiScale(roi_gray)
        
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (255, 0 ,0), 5)
        
        #for (sx, sy, sw, sh) in smiles:
            #cv2.rectangle(roi_color, (sx,sy), (sx+sw, sy+sh), (0, 0, 255), 5)
            
        #for (mx, my, mw, mh) in mouth:
            #cv2.rectangle(roi_color, (mx,my), (mx+mw, my+mh), (255, 0, 255), 5)
            
    # Display
    cv2.imshow('img', img)
    # Stop if escape key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the VideoCapture object
cap.release()
cv2.destroyAllWindows()
