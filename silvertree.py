
'''                 *** RUN ON PC ***
This code show colored recursive tree. It based on Turtle graphics. '''

from turtle import *
from random import random
import time

bgcolor("black")
lt(90)
def fr(w):
    
    if  w >= 0.8:
        
        pensize(w)
        fd(w *10)
        rt(30)
        fr(w*0.75)
        lt(60)
        fr(w*0.75)
        rt(30)
        bk(w*10)
        pensize(w)
    
        if 0.00000000000001 <= w >= 0.00000000000009:
            circle(2)
    
    
    if 0.1 <= w >= 0.35:
        color("silver")
    if 0.36 <= w>= 1.9:
            color("silver")
    if 2 <= w >= 3:
        color("silver")
    if 3.1 <= w >= 6:
        color("silver")
  
speed(0)
color("silver")
resizemode("user")
"""image = "rating_on.gif"
addshape(image)"""
shape()
penup()
goto(0, -200)
pendown()
time.sleep(0)
fr(10)


