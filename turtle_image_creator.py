import cv2
import turtle as trtl
import numpy as np
from multiprocessing import Process
import os

## import image and create x and y / width and height variables
image= cv2.imread("portrait.JPG")
x=image.shape[1]
y=image.shape[0]
width= int(x/70)
height= int(y/70)
print(width,height)
image= cv2.resize(image, dsize=(width,height))
image= cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
x=image.shape[0]
y=image.shape[1]


## create turtle instance and init painter variables
painter= trtl.Turtle()
painter.speed(10)

## create screen then adjust settings
wn= trtl.Screen()
wn.setup(width= x+100,height= y+200, startx=-x-100, starty=y+100)
wn.colormode(255)

y_pos= y
x_pos= -x
painter.penup()
painter.goto(x_pos,y_pos)
painter.pendown()

def create_row(segment):
    new_painter=trtl.Turtle()
    

"""
segments= 5

for segment in range(segments):
    p=Process(target=create_row, args=(segment))

"""


while y_pos >= -y:
    for row in image:
        for pixel in row:
            painter.color(tuple(pixel))
            painter.forward(1)
            x_pos+=1
        x_pos=-x
        painter.penup()
        painter.goto(x_pos,y_pos)
        painter.pendown()
        y_pos-=1
            #painter.color(pixel)
print("hey")

wn.mainloop()