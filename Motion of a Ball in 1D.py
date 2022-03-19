from vpython import *
from time import *

ceiling=box(pos=vector(0,5,0),color=color.blue,length=10,width=10,height=.1)
floor=box(pos=vector(0,-5,0),color=color.blue,length=10,width=10,height=.1)
left=box(pos=vector(-5,0,0),color=color.blue,length=.1,width=10,height=10)
right=box(pos=vector(5,0,0),color=color.blue,length=.1,width=10,height=10)
back=box(pos=vector(0,0,-5),color=color.blue,length=10,width=.1,height=10)
marble=sphere(color=color.red,radius=.75)

deltax=.1
xpos=0

while True:
    rate(50)

    xpos+=deltax

    if xpos>=4.25 or xpos<=-4.25:
        deltax=-deltax
    
    marble.pos=vector(xpos,0,0)
