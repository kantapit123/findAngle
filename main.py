# Python program to create
# a file explorer in Tkinter
  
# import all components
# from the tkinter library
#from fileinput import filename
import imghdr
from tkinter import *
from tkinter import filedialog
from turtle import onclick
from typing_extensions import Self
import cv2
import math
# importing all files  from tkinter
from doctest import master
from tkinter import ttk
  
# import only asksaveasfile from filedialog
# which is used to save file in any extension
from tkinter.filedialog import asksaveasfile,askdirectory,SaveAs, asksaveasfilename

from cv2 import imread
#from popup import mainWindow

# Function for opening the
# file explorer window
#C:\Users\watch\OneDrive - Suranaree University of Technology\Plz learnCode\findAngle

def cal(filename):
    img = cv2.imread(filename)
    
    #dsize = (int(img.shape[1] * 80 / 100),int(img.shape[0] * 80 / 100))
    dsize = (1080, 972)
    img_resize = cv2.resize(img, dsize)
    img = img_resize
    save_img = img
    pointsList = []
    intersection_point = []
    def mousePoints(event,x,y,flags,params):
        if event == cv2.EVENT_LBUTTONDOWN:
            size = len(pointsList)
            text = str(x)+','+str(y)
            cv2.putText(img, text,(x,y),0,0.3,(255,0,0),1)
            cv2.circle(img,(x, y),5, (0,0,255), cv2.FILLED)
            pointsList.append([x,y])
            if size >= 3:
                #cv2.line(img,tuple(pointsList[round((size-1)/3)*3]),(x,y),(0,0,255),2)
                #cv2.line(img,pointsList[size-1],(x, y),(0,255,0),2)
                fullLine(pointsList)
                line1 = [pointsList[0],pointsList[1]]
                line2 = [pointsList[2],pointsList[3]]
                intersection_point.append(line_intersection(line1,line2))
                cv2.circle(img,intersection_point[0],5, (0,0,255), cv2.FILLED)
                #print(intersection_point)
            #print(pointsList)

    def line_intersection(line1, line2):
        xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
        ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

        def det(a, b):
            return a[0] * b[1] - a[1] * b[0]

        div = det(xdiff, ydiff)
        if div == 0:
            raise Exception('lines do not intersect')

        d = (det(*line1), det(*line2))
        x = round(det(d, xdiff) / div)
        y = round(det(d, ydiff) / div)
        return [x, y]

    def fullLine(pointsList): #(x,y)
        pt1, pt2, pt3, pt4 = pointsList[:4]
        m1 = gradient(pt1, pt2) #pt1 to ptn
        m2 = gradient(pt3, pt4)
        y1 = round(((m1*(pt1[0] - 0) - pt1[1]))*(-1))
        y2 = round(((m2*(pt3[0] - 0) - pt3[1]))*(-1))
        y3 = round(((m1*(1080 - pt1[0]) + pt1[1])))
        y4 = round(((m2*(1080 - pt3[0]) + pt3[1])))
        ptf1 = (0, y1)
        ptf2 = (0, y2)
        ptf3 = (1080, y3)
        ptf4 = (1080, y4)
        # m2 = gradient(pt1, pt2)# pt1 to pt2
        # angR = math.atan((m2-m1)/(1+m2*m1))
        # angD = round(math.degrees(angR))
        # a = round((math.tan(angD))*(pt1[0]))
        cv2.line(img,pt1,ptf1,(0,255,0),2)
        cv2.line(img,pt1,pt2,(0,255,0),2)
        cv2.line(img,pt3,ptf2,(0,255,0),2)
        cv2.line(img,pt3,pt4,(0,255,0),2)
        cv2.line(img,pt2,ptf3,(0,255,0),2)
        cv2.line(img,pt4,ptf4,(0,255,0),2)

    def gradient(pt1, pt2):
        return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

    def getAngle(pointsList, intersection_point):
        pt1 = intersection_point[0]
        pt2 = pointsList[0]
        pt3 = pointsList[2]
        m1 = gradient(pt1, pt2)
        m2 = gradient(pt1, pt3)
        angR = math.atan((m2-m1)/(1+m2*m1))
        angD = round(math.degrees(angR))
        #print(angD)
        cv2.putText(img, str(angD),(pt1[0]-40,pt1[1]-20), cv2.FONT_HERSHEY_COMPLEX, 1.5, (0,0,255),2)
        #print(m1, m2 ,angR, angD)
        #print(pt1, pt2, pt3)
        #print("angle")

    def askSavemainWindow(object, file):
        # root = Tk()
        # root.title('Do you want to save the process?')
        # root.geometry("400x100+500+250")
        root = object

        btn1 = ttk.Button(root, text = 'Save', command = lambda : save(root, file))
        btn1.pack(padx=30, pady=10, side= LEFT)

        btn2= ttk.Button(root,text="Don't save", command = lambda : dontSave(root))
        btn2.pack(padx=30, pady=10, side= LEFT)

        btn3 = ttk.Button(root,text="Cancel", command = lambda : cancel(root))
        btn3.pack(padx=30, pady=10, side= LEFT)
        # root.mainloop()
    def save(object, save_img):
        root = object
        files = [('JPG', '*.jpg'),
                ('PNG', '*.png'),
                ('All Files', '*.*'),]
                #  ('Python Files', '*.py'),
                #  ('Text Document', '*.txt'),
        file = asksaveasfilename(filetypes = files, defaultextension = files, )
        #print(file)
        cv2.imwrite(file,save_img)
        cv2.destroyAllWindows()
        root.destroy()
    def dontSave(object):
        root = object
        root.destroy()
        cv2.destroyAllWindows()

    def cancel(object):
        root = object
        root.destroy()

    def resize_img(src):
        dsize = (int(src.shape[1] * 80 / 100),int(src.shape[0] * 80 / 100))
        img_resize = cv2.resize(src, dsize)
        return img_resize
    #main in cal
    while True:
        if len(pointsList) % 4 == 0 and len(pointsList) != 0:
            getAngle(pointsList, intersection_point)
        if len(pointsList) > 4:
            pointsList = []
            intersection_point = []
            #img = img_resize
            img = resize_img(cv2.imread(filename))
            
        cv2.imshow('Image',img)
        cv2.setMouseCallback('Image',mousePoints)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            pointsList = []
            intersection_point = []
            img = resize_img(cv2.imread(filename))
            #img = cv2.resize(img, dsize)
        if cv2.waitKey(1) & 0xFF == ord('s'): #safe
            cv2.destroyAllWindows()
            break;
        if cv2.waitKey(1) & 0xFF == 27: #ESC
            #ask2SavePopUp()
            #cv2.imwrite('/path/to/destination/image.png',image)
            root = Tk()
            root.title('Do you want to save the process?')
            root.geometry("400x100+500+250")
            save_img = img
            askSavemainWindow(root, save_img)
            root.mainloop()


def openFile():
    filename = filedialog.askopenfilename(title = "Select a File",filetypes = (("all files","*.*"),("Text files","*.txt*")))
    #filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("all files","*.*"),("Text files","*.txt*")))
    if filename != "":
        label_file_explorer.configure(text="File Opened: "+filename)
        #img = cv2.imread(filename)
        cal(filename)
        #cv2.imshow('Image',img)
    else:
        label_file_explorer.configure(text="Please Select a File")

#main
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
                        text = "Open Files",
                        command = openFile)
  
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