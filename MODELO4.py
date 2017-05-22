#MODELO HULK 4
#Impulso Inicial

import math
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def Impulso(y,t):
        Qx = y[0]
        Qy = y[1]
        
        dQxdt = FRx 
        dQydt = FRy
       
        return[dQxdt,dQydt]
                          
# Condições do ambiente
g = 9.8                     # Gravidade

#Parâmetros Hulk
Fmuscular = 2458624.420     # Força Muscular do Hulk  
M = (Fmuscular/2)*(2**0.5)  # Força Muscular vezes sin(45)
m = 1100                    # Massa Hulk
deltaT = 1                  # Tempo de Impulso

# Força Peso
P = m*g

# Força Elástica
k = 10000                   # Constante da 'Mola'
x = 1.0                     # Varição de alturas
Felp = k*x
Felpx = Felp*math.cos((math.pi)/4) # em x
Felpy = Felp*math.sin((math.pi)/4) # em y

# Força de Atrito
u = 0.5                         # Coeficiente de atrito
N = m*g                         # Normal = Peso (plano reto)
Fat = u*N                       
d = 100                         # distância percorrida correndo (V0 = 0)
Vfat = ((2*d*(Fmuscular-Fat))/m)**0.5  # Velocidade final chegada com o atrito

# Forças Resultantes xy
FRy = M+Felpy                   # em y
V0y = FRy*deltaT/m              # velocidade inicial em y

FRx =(M + Felpx - Fat)          # em x
V0x = ((FRx)*deltaT + m*Vfat)/m # velocidade inicial em x

#Resolução Odeint

tempoI1 = np.arange(0,1,0.01)                                                           # Tempo de Durção do 1 Salto
y0 = [m*Vfat,0]              # Condições Iniciais
Imp1 = odeint(Impulso,y0,tempoI1)                                                        # Resolução Odeint

plt.plot(tempoI1,Imp1[:,0],)
plt.xlabel("Tempo")
plt.ylabel("Quantiadde de Movimento em x")
plt.title("Qx por tempo")
plt.show()


plt.plot(tempoI1,Imp1[:,1],)
plt.xlabel("Tempo")
plt.ylabel("Quantiadde de Movimento em y")
plt.title("Qy por tempo")
plt.show()

