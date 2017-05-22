# MODELO HULK 5
# Impulso Final

import math
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def Impulso2(y,tempoI2):
        
        Qx = y[0]
        Qy = y[1]
        dQxdt = FRx2 
        dQydt = FRy2

        return[dQxdt,dQydt]

# Condições para o Impulso2
tempoI2 = np.arange(0,1,0.01)   # Tempo de Durção do 1 Salto

# Condições do ambiente
g = 9.8                     # Gravidade

#Parâmetros Hulk
Fmuscular = 2458624.420     # Força Muscular do Hulk  
M = (Fmuscular/2)*(2**0.5)  # Força Muscular vezes sin(45)
m = 1100                    # Massa Hulk
deltaT = 1                  # Tempo de Impulso

# Força de Atrito
u = 0.5                         # Coeficiente de atrito
N = m*g                         # Normal = Peso (plano reto)
Fat = u*N                       
d = 100                         # distância percorrida correndo (V0 = 0)
Vfat = ((2*d*(Fmuscular-Fat))/m)**0.5  # Velocidade final chegada com o atrito


# Força Peso
P = m*g

# Força Elástica
k = 10000                   # Constante da 'Mola'
x = 1.0                     # Varição de alturas
Felp = k*x
Felpx = Felp*math.cos((math.pi)/4) # em x
Felpy = Felp*math.sin((math.pi)/4) # em y

# Forças Resultantes xy
FRy = M + Felpy                 # Impulso1 em y
FRy2 = M + Felpy - P            # Impulso2 em y
V0y = FRy*deltaT/m              # velocidade inicial em y
Vary = -1945.93004976           # Velocidade ar finaal y

FRx =(M - Felpx - Fat)          # Impulso1 em x
FRx2 =(M - Felpx - Fat)         # Impulso2 em x
V0x = ((FRx)*deltaT + m*Vfat)/m # velocidade inicial em x
Varx =  20.3998668529           # velocidade final em y
        
# Força resistencia ar 
dar = 1.2                       # Densidade do ar
Ahulk = 6                       # Área do Hulk (Retângulo: 2x3)
Cd = 0.75                       # Coeficiente de arrasto
k = 0.5*Cd*Ahulk*1.2            # Constante simplificada ar

#Resolução Odeint

y0 = [Varx,Vary]                   # Condições Iniciais
Imp2 = odeint(Impulso2,y0,tempoI2) # Resolução Odeint

plt.plot(tempoI2,Imp2[:,0],)
plt.xlabel("Tempo")
plt.ylabel("Quantidade de Movimento em x")
plt.title("Qx por tempo")
plt.show()

plt.plot(tempoI2,Imp2[:,1],)
plt.xlabel("Tempo")
plt.ylabel("Quantidade de Movimento em y")
plt.title("Qy por tempo")
plt.show()
