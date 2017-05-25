#MODELO HULK 8

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
	dvxdt = -k*(Vx*(Vx**2 + Vy**2)**(0.5))/m
	dydt = Vy
	dvydt = -(P + k*(Vy*(Vx**2 + Vy**2)**(0.5)))/m
	
	return[dxdt,dvxdt,dydt,dvydt]
                  
# Condições do ambiente
g = 9.8                     # Gravidade

#Parâmetros Hulk
m = 1100                    # Massa Hulk


# Força Peso
P = m*g



# Força de Atrito
u = 0.5                         # Coeficiente de atrito
N = m*g                         # Normal = Peso (plano reto)
Fat = u*N

# Velocidade Iniciais
V0y = 211.214615209 
V0x = 200.118766411 # velocidade inicial em x

# Força resistencia ar 
dar = 1.2                       # Densidade do ar
Ahulk = 6                       # Área do Hulk (Retângulo: 2x3)
Cd = 0.75                       # Coeficiente de arrasto
k = 0.5*Cd*Ahulk*1.2            # Constante simplificada ar

#Resolução Odeint
x0 = 1535.93915913
y0 = 0

tempo = np.arange(0,17.51,0.01)  # Tempo de Durção do 1 Salto
y0 = [x0,V0x,y0,V0y]              # Condições Iniciais
Sol = odeint(EqDif,y0,tempo)    # Resolução Odeint
print(Sol[:,1][-1],Sol[:,3][-1],Sol[:,0][-1],Sol[:,2][-1])
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
