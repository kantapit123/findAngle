import cv2
import math

path = 'S__11485196.jpg'
img = cv2.imread(path)
pointsList = []
intersection_point = []
sizeofscr = 1350*1215
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
            print(intersection_point)
        print(pointsList)
        
        #print(x, y)
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
    ptf1 = (0,y1)
    ptf2 = (0,y2)
    # m2 = gradient(pt1, pt2)# pt1 to pt2
    # angR = math.atan((m2-m1)/(1+m2*m1))
    # angD = round(math.degrees(angR))
    # a = round((math.tan(angD))*(pt1[0]))
    cv2.line(img,pt1,ptf1,(0,255,0),2)
    cv2.line(img,pt1,pt2,(0,255,0),2)

    cv2.line(img,pt3,ptf2,(0,255,0),2)
    cv2.line(img,pt3,pt4,(0,255,0),2)
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

while True:

    if len(pointsList) % 4 == 0 and len(pointsList) != 0:
        getAngle(pointsList, intersection_point)



    cv2.imshow('Image',img)
    cv2.setMouseCallback('Image',mousePoints)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pointsList = []
        intersection_point = []
        img = cv2.imread(path)
    if cv2.waitKey(1) & 0xFF == ord('x'):
        break;