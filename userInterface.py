# Python program to create
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
from fileinput import filename
from tkinter import *
# import filedialog module
from tkinter import filedialog
from typing_extensions import Self
#import findAng
import cv2
# Function for opening the
# file explorer window
#C:\Users\watch\OneDrive - Suranaree University of Technology\Plz learnCode\findAngle


def browseFile():
    filename = filedialog.askopenfilename(title = "Select a File",filetypes = (("all files","*.*"),("Text files","*.txt*")))
    #filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("all files","*.*"),("Text files","*.txt*")))
    if filename != "":
        label_file_explorer.configure(text="File Opened: "+filename)
        img = cv2.imread(filename)
        return img
        #cv2.imshow('Image',img)
    else:
        label_file_explorer.configure(text="Please Select a File")
def cal(filename):
    label_file_explorer.configure(filename)
    cv2.imshow('Image',filename)                                                  
# Create the root window
window = Tk()
  
# Set window title
window.title('Find Angle Program')
  
# Set window size
window.geometry("700x200+500+250")
  
#Set window background color
window.config(background = "white")
  
# Create a File Explorer label
label_file_explorer = Label(window,
                            text = "File Explorer using Tkinter",
                            width = 100, height = 4,
                            fg = "blue")
  
      
button_explore = Button(window,
                        text = "Browse Files",
                        command = browseFile)
  
button_exit = Button(window,
                     text = "Exit",
                     command = exit)
  
# Grid method is chosen for placing
# the widgets at respective positions
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)
button_explore.grid(column = 1, row = 2)
button_exit.grid(column = 1,row = 3)


# Let the window wait for any events
window.mainloop()