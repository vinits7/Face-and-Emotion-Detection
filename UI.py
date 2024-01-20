from tkinter import *
import tkinter.font as font
import os


root=Tk()
root.title("Attendance System")

def click1():
	os.system("python C:\\Users\\PALAKT~1\\Desktop\\2001CS84-Palak_Project\\2001CS84_Code\\temp2.py")

def click2():
	os.system("C:\\Users\\PALAKT~1\\Desktop\\2001CS84-Palak_Project\\2001CS84_Code\\at\\attendence.csv")


head=Label(root, text="ATTENDANCE SYSTEM", anchor=CENTER, padx=10, pady=10, font=("Arial", 40))
head.grid(row=1, column=1, columnspan=5, sticky="nsew")

op1=Button(root,font=("Arial", 10), text="Capture Attendance", fg="white", bg="black", height="3", pady=20, command=lambda: click1())
op1.grid( row="2", column="3", sticky="nsew",padx=10, pady=10)

op2=Button(root,font=("Arial", 10), text="View Record", fg="white", bg="black", height="3", pady=20, command=lambda: click2())
op2.grid( row="3", column="3", sticky="nsew",padx=10, pady=10)


root.mainloop()
