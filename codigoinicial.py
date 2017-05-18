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
	dvxdt = -k*(Vx**2)/m
	dydt = Vy
	dvydt = -(m*g + k*(Vy**2))/m
	
	return[dxdt,dvxdt,dydt,dvydt]
                  
tempo = np.arange(0,19.8,0.01)

M = 1738510 # Força Muscular vezes sin(45)
m = 1100    # Massa Hulk
k = 10000   # Constante da 'Mola'
x = 1.0     # Varição de alturas
g = 9.8     # Gravidade
deltaT = 1  # Tempo de Impulso

# Forças Resultantes xy
FRy = M+k*x*math.sin((math.pi)/4)
V0y = FRy*deltaT/m

FRx =(M + k*x*math.sin((math.pi)/4))
V0x = (FRx/m)*deltaT

# Força resistencia ar 
dar = 1.2
Ahulk = 6
Cd = 0.75                  
k = 0.5*Cd*Ahulk*1.2
y0 = [0,V0x,0,V0y]
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
