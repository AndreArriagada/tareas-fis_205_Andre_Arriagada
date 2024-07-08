GlowScript 2.9 VPython

G=6.67e-11 
mass=7.342e22 #kg
rem=384.4e6 #m

A=sphere(pos=vector(0,0,0), radius=rem/20, color=color.white, make_trail=True)
B=sphere(pos=vector(rem, 0, 0), radius=rem/20, color=color.blue, make_trail=True)
#C=sphere(pos=vector(rem,0,0), radius=rem/15, color=color.yellow, make_trail=True)
axis_length = rem
shaft_thickness = rem / 40  #  valor para cambiar el grosor de los ejes
x_axis = arrow(pos=vector(0, 0, 0), axis=vector(axis_length, 0, 0), color=color.red, shaftwidth=shaft_thickness)
y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, axis_length, 0), color=color.green, shaftwidth=shaft_thickness)


A.m=4*mass
B.m=4*mass
#C.m=2.5*mass

A.p=A.m*vector(0,100,0)
B.p=B.m*vector(0,-100,0)
#C.p=C.m*vector(0,20,0)


t=0
dt=3600

tmax=24*28*dt*1000

while t<tmax:
  rate(100)
  rAB=B.pos-A.pos
  #rAC=C.pos-A.pos
  #rBC=C.pos-B.pos
  
  FAB=-G*A.m*B.m*norm(rAB)/mag(rAB)**2
  #FAC=-G*A.m*C.m*norm(rAC)/mag(rAC)**2
  #FBC=-G*B.m*C.m*norm(rBC)/mag(rBC)**2
  
  A.p=A.p+(-FAB)*dt
  B.p=B.p+(FAB)*dt
  #C.p=C.p+(FAC+FBC)*dt
  
  A.pos=A.pos+A.p*dt/A.m
  B.pos=B.pos+B.p*dt/B.m
  #C.pos=C.pos+C.p*dt/C.m
  
  t=t+dt
