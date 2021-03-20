


# PROJECT BY RACHEL C.N- IOT AND COMPUTER VISION INTERN AT THE SPARKS FOUNDATION- MARCH 2021

# importing libraries

import numpy as np
import pandas as pd
import cv2

# Defining the image used

image = cv2.imread("color.jpeg")

# Importing CSV file with names of colours and their RGB, hex Values and naming columns in the CSV file

index=["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('colors.csv', names=index, header=None)

#Defining global variables - needed while working on aplication

clicked = False
r = g = b = xpos = ypos = 0

# This function will be called when when we double click on an area on the image
#It returns the Name of the colour with it's RGB Value.

def recognize_color(R,G,B):
    minimum = 10000
    for i in range(len(csv)):
        # This line tries to find the nearest color using RGB values, KNN algorithm
        m = abs(R- int(csv.loc[i,"R"])) + abs(G- int(csv.loc[i,"G"]))+ abs(B- int(csv.loc[i,"B"]))
        if(m<=minimum):
            minimum = m
            name = csv.loc[i,"color_name"]
    return name

# Defining the Double click function- Color name is displayed when a region in the image is double clicked

def double_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = image[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

# Creating the application

# Open the image as a new file using OpenCV

cv2.namedWindow('Color Recognition App')

# Calling the Double click function that we created
cv2.setMouseCallback('Color Recognition App', double_click)

# While loop to start Application window working

while(1):
  cv2.imshow("Color Recognition App",image)
  if (clicked):
   
        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        cv2.rectangle(image,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        txt = recognize_color(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv2.putText(image, txt,(50,50),4,0.8,(255,255,255),2,cv2.LINE_8)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv2.putText(image, txt,(50,50),2,0.8,(0,0,0),2,cv2.LINE_8)
            
        clicked=False


#Break the loop when user hits 'esc' key--ASCII value of esc is 27
        
  if cv2.waitKey(20) & 0xFF ==27:
     break

# Destroy all windows

cv2.destroyAllWindows()




