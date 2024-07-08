GlowScript 2.9 VPython

G = 6.67e-11
rem =384400000  # m

# Esferas que representan los cuerpos
A = sphere(pos=vector(0, 0, 0), radius=rem/50,       color=color.white, make_trail=True)
B = sphere(pos=vector((1/2)*rem,0,0), radius=rem/50, color=color.blue, make_trail=True)
C = sphere(pos=vector(rem, 0, 0), radius=rem/50,     color=color.yellow, make_trail=True)

A.m = 100*7.35e22
B.m =100*7.35e22
C.m = 50*7.35e22

A.p = A.m * vector(0,-1000, 0)
B.p = B.m * vector(0, 0 , 0)
C.p = C.m * vector(0, 1000, 0)

# Creamos ejes visibles
axis_length = rem
shaft_thickness = rem / 50  #  valor para cambiar el grosor de los ejes
x_axis = arrow(pos=vector(0, 0, 0), axis=vector(axis_length, 0, 0), color=color.red, shaftwidth=shaft_thickness)
y_axis = arrow(pos=vector(0, 0, 0), axis=vector(0, axis_length, 0), color=color.green, shaftwidth=shaft_thickness)


t = 0
dt = 3600
#tiempo hasta el cual correrá la simulación
tmax =dt * 10000000

while t < tmax:
    rate(20)
#vectores de posicion
    rAB = B.pos - A.pos
    rAC = C.pos - A.pos
    rBC = C.pos - B.pos
#fuerza de atracción entre pares
    FAB = -G * A.m * B.m * norm(rAB) / mag(rAB)**2
    FAC = -G * A.m * C.m * norm(rAC) / mag(rAC)**2
    FBC = -G * B.m * C.m * norm(rBC) / mag(rBC)**2
#momentum de los cuerpos
    A.p = A.p + (-FAB - FAC) * dt
    B.p = B.p + (FAB - FBC) * dt
    C.p = C.p + (FAC + FBC) * dt
#actualizamos la posición de los cuerpos
    A.pos = A.pos + A.p * dt / A.m
    B.pos = B.pos + B.p * dt / B.m
    C.pos = C.pos + C.p * dt / C.m
#actualizamos el tiempo de la iteración
    t = t + dt
