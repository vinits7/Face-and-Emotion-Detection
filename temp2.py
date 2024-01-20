import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime

path = r"C:\Users\Palak Totala\Desktop\2001CS84-Palak_Project\2001CS84_Code\student_images"    # Path to folder that stores images of students. 
																							   # File name is student's name

images = [] # list to store image arrays
classNames = [] # list to store file names aka student names

mylist = os.listdir(path) # list of all files in the path folder

for cl in mylist: # for all files in the folder
	curImg = cv2.imread(f'{path}/{cl}') # takes the image as input and decodes into a matrix with the color 
										# channels stored in the order of Blue, Green, Red, and A respectively
	images.append(curImg) # adds the image matrix in the images list
	classNames.append(os.path.splitext(cl)[0]) # adds the filename in the classNames list

# f-string : f-string is really an expression evaluated at run time, not a constant value (doubt)

# For face recognition, the algorithm notes certain important measurements on the face — 
# like the color and size and slant of eyes, the gap between eyebrows, etc. 
# All these put together define the face encoding — the information obtained out of the image — 
# that is used to identify the particular face.

def findEncodings(images): # function to encode all the images and store them in a variable encoded_face_train. 
	encodeList = [] # list to store face encodings
	for img in images:
		img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
		encoded_face = face_recognition.face_encodings(img)[0]  # face_recognition.face_encodings(known_image) basically returns 
																# a list of 128-dimensional face encodings (one for each face in the image)
																# Now, you are using the index [0] to get the first found face. 
		encodeList.append(encoded_face)
	return encodeList

encoded_face_train = findEncodings(images)

def markAttendance(name):
	with open('C:\\Users\\Palak Totala\\Desktop\\2001CS84-Palak_Project\\2001CS84_Code\\at\\attendence.csv','r+') as f: # the file is closed when the block 
																								# inside the with statement is exited.
		myDataList = f.readlines() # returns a list containing each line in the file as a list item
		nameList = [] # A list to store names of students whose attendence is registered in the file
		datelist = []
		#print(nameList)

		for line in myDataList:
			entry = line.split(',')
			nameList.append(entry[0])

		if name not in nameList:        
			now = datetime.now()
			time = now.strftime('%I:%M:%S:%p')
			date = now.strftime('%d-%B-%Y')
			f.writelines(f'{name}, {time}, {date}\n')

# To capture video from webcam. 
cap  = cv2.VideoCapture(0) #This will return video from the first webcam on your computer.
# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')

while True: #initiates an infinite loop

	success, img = cap.read()   # Returns a bool (True/False). If the frame is read correctly, it will be True.
								# Reads the frame and captures an image img.

	imgS = cv2.resize(img, (0,0), None, 0.25,0.25)  # Resize the image by 1/4 only for the recognition part. 
													# output frame will be of the original size.
													# Resizing improves the Frame per Second.

	imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

	faces_in_frame = face_recognition.face_locations(imgS)  # returns a list of tuples of found face locations in css 
															# (top, right, bottom, left) order

	encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)
													# Parameter 1 : face_image – The image that contains one or more face
													# Parameter 2 : known_face_locations – Optional - the bounding boxes of 
													#               each face if you already know them.

	for encode_face, faceloc in zip(encoded_faces,faces_in_frame): # for each encoded face in the frame

		matches = face_recognition.compare_faces(encoded_face_train, encode_face) 
		faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
		matchIndex = np.argmin(faceDist)
		print(matchIndex)
   
		if matches[matchIndex]:
			name = classNames[matchIndex].upper().lower()
			y1,x2,y2,x1 = faceloc
			# since we scaled down by 4 times
			y1, x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
			cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
			cv2.rectangle(img, (x1,y2-35),(x2,y2), (0,255,0), cv2.FILLED)
			cv2.putText(img,name, (x1+6,y2-5), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
			markAttendance(name)

	cv2.imshow('webcam', img)   # displays the image on a window named webcam, and since there 
								# is an infinite loop of images it is a live video
	
	# Stop if escape key is pressed
	k = cv2.waitKey(30) & 0xff 
	# cv2.waitKey() returns a 32-bit integer that is the ASCII value of the key pressed.
	# 0xFF is a hexadecimal constant which is 11111111 in binary. 
	# By using bitwise AND (&) with this constant, it leaves only the last 8 bits of the original
	# We only need last 8 digits since ASCII value of the character can be maximum 255.

	if k==27: #27 is the ASCII value of the esc key.
		break
# Release the VideoCapture object
cap.release()

