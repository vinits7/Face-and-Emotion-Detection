# importing the necessary modules
import numpy as np
import cv2
import tensorflow as tf

#importing the cascade file to train the model
face_detection = cv2.CascadeClassifier('C:\\Users\\VINIT\\Downloads\\emotion\\haarcascade_frontalface_default.xml')

#cv2 commands to capture live video and define the frame size of video screen
camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
settings = {
    'scaleFactor': 1.3, 
    'minNeighbors': 5, 
    'minSize': (50, 50)
}

# labelling the emotions
labels = ["Neutral","Happy","Sad","Surprise","Angry"]

# importing the keras model for emotion recognition 
model = tf.keras.models.load_model('C:\\Users\\VINIT\\Downloads\\emotion\\best_model.h5')

while True:
    ret, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # making images grayscale from colored
    detected = face_detection.detectMultiScale(gray, **settings) # detecting the face 
    
    # drawing a rectangle around the co-ordinates of detected faces 
    for x, y, w, h in detected:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,0),2) # (image, co-ordinates of detected face, color, thickness)
        cv2.rectangle(img, (x, y), (x+w//3, y+20), (127,0,255),-1) # drawing a rectangle for the emotion label
        face = gray[y+5:y+h-5, x+20:x+w-20]
        face = cv2.resize(face, (48,48)) 
        face = face/255.0

        predictions = model.predict(np.array([face.reshape((48,48,1))])).argmax() # predicts the emotion 
        state = labels[predictions] 
        font = cv2.FONT_HERSHEY_SIMPLEX #font for the label
        cv2.putText(img,state,(x+10,y+15), font, 0.5, (255,255,255), 2, cv2.LINE_AA) 

    cv2.imshow('Facial Expression', img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    if cv2.waitKey(5) != -1:
        break
        
camera.release()
cv2.destroyAllWindows()