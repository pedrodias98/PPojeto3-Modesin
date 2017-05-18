import math
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def EqDif (Y,t):
	x = Y[0]
	Vx = Y[1]
	y = Y[2]
	Vy = Y[3]
	dxdt = Vx
	dvxdt = 0
	dydt = Vy
	dvydt = -g
	
	return[dxdt,dvxdt,dydt,dvydt]
tempo = np.arange(0,330,0.01)
M = 1738510
m = 1100
k = 10000
x = 1.7
g = 9.8
deltaT = 1
I = M+k*x 
Vy = +I*deltaT/m 
Vx = (M/m)*deltaT/m 

y0 = [0,Vx,0,Vy]
Sol = odeint(EqDif,y0,tempo)

plt.plot(tempo,Sol[:,2],)
plt.xlabel("Tempo")
plt.ylabel("altura")
plt.title("Altura máxima por tempo")
plt.show()

plt.plot(tempo,Sol[:,0],)
plt.xlabel("Tempo")
plt.ylabel("distância")
plt.title("Distância máxima por tempo")
plt.show()

plt.plot(tempo,Sol[:,1],)
plt.xlabel("Tempo")
plt.ylabel("Velocidade em x")
plt.title("Velocidade em x por tempo")
plt.show()

plt.plot(tempo,Sol[:,3],)
plt.xlabel("Tempo")
plt.ylabel("Velocidade em y")
plt.title("Velocidade em y por tempo")
plt.show()