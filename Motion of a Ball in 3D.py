from vpython import *
from time import *

ceiling=box(pos=vector(0,5,0),color=color.cyan,length=10,width=10,height=.1)
floor=box(pos=vector(0,-5,0),color=color.cyan,length=10,width=10,height=.1)
left=box(pos=vector(-5,0,0),color=color.cyan,length=.1,width=10,height=10)
right=box(pos=vector(5,0,0),color=color.cyan,length=.1,width=10,height=10)
back=box(pos=vector(0,0,-5),color=color.cyan,length=10,width=.1,height=10)
marble=sphere(color=color.orange,radius=.75)

deltax=.4
xpos=0
deltay=.3
ypos=1
deltaz=.2
zpos=-1

while True:
    rate(50)

    xpos+=deltax
    ypos+=deltay
    zpos+=deltaz

    if xpos>=4.25 or xpos<=-4.25:
        deltax=-deltax
    if ypos>=4.25 or ypos<=-4.25:
        deltay=-deltay
    if zpos>=4.25 or zpos<=-4.25:
        deltaz=-deltaz
    
    marble.pos=vector(xpos,ypos,zpos)
