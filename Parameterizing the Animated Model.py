
from vpython import *
from time import *

mradius=.5
roomwidth=12
roomdepth=20
roomheight=4
wallthickness=.1

ceiling=box(pos=vector(0,roomheight/2,0),color=color.green,size=vector(roomwidth,wallthickness,roomdepth))
floor=box(pos=vector(0,-roomheight/2,0),color=color.white,size=vector(roomwidth,wallthickness,roomdepth))
left=box(pos=vector(-roomwidth/2,0,0),color=color.blue,size=vector(wallthickness,roomheight,roomdepth))
right=box(pos=vector(roomwidth/2,0,0),color=color.yellow,size=vector(wallthickness,roomheight,roomdepth))
back=box(pos=vector(0,0,-roomdepth/2),color=color.cyan,size=vector(roomwidth,roomheight,wallthickness))
marble=sphere(color=color.red,radius=mradius)

deltax,deltay,deltaz=.1,.1,.1
xpos,ypos,zpos=0,1,-1

while True:
    rate(50)

    xpos+=deltax
    ypos+=deltay
    zpos+=deltaz

    xrme=xpos+mradius
    ytme=ypos+mradius
    zfme=zpos+mradius
    xlme=xpos-mradius
    ybme=ypos-mradius
    zbme=zpos-mradius

    rwe=roomwidth/2-wallthickness/2
    lwe=-roomwidth/2+wallthickness/2
    twe=roomheight/2-wallthickness/2
    bowe=-roomheight/2+wallthickness/2
    fwe=roomdepth/2-wallthickness/2
    bawe=-roomdepth/2+wallthickness/2

    if xrme>rwe or xlme<lwe:
        deltax=-deltax
    if ytme>twe or ybme<bowe:
        deltay=-deltay
    if zfme>fwe or zbme<bawe:
        deltaz=-deltaz
        
    marble.pos=vector(xpos,ypos,zpos)
