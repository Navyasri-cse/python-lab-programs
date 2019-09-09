import math
def ball_collide(x1,y1,r1,x2,y2,r2):
    dist=math.sqrt((x2-x1)**2+(y2-y1)**2);
    print("Distance b/w two balls:",dist)
    r=r1+r2;
    print("Sum of radius",r)
    if(dist<=r):
        return True
    else:
        return False
    
x1,y1=input("enter the position of first ball x1,y1").split()
r1=int(input("enter the radius of first ball"))

x2,y2=input("enter the position of second ball x2,y2").split()
r2=int(input("enter the radius of second ball"))
x1=int(x1)
y1=int(y1)
x2=int(x2)
y2=int(y2)
if(ball_collide(x1,y1,r1,x2,y2,r2)):
    print("balls are colliding")
else:
    print("balls are not colliding")
