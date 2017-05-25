#MODELO HULK 4
#Impulso Inicial

import math
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt

def Impulso(I,tempoI1):
        x = I[0]
        Vx = I[1]
        y = I[2]
        Vy = I[3]
        dxdt = Vx
        dVxdt = -k*(math.sqrt(x**2 + y**2) + math.sqrt(x0**2 + y0**2))*x/math.sqrt(x**2 + y**2) - Fat
        dydt = Vy
        dVydt = -k*(math.sqrt(x**2 + y**2) + math.sqrt(x0**2 + y0**2))*y/math.sqrt(x**2 + y**2) - P
        return[dxdt,dVxdt,dydt,dVydt]
                          
# Condições do ambiente
g = 9.8                     # Gravidade

#Parâmetros Hulk
Fmuscular = 2458624.420     # Força Muscular do Hulk  
M = (Fmuscular/2)*(2**0.5)  # Força Muscular vezes sin(45)
m = 1100                    # Massa Hulk


# Força Peso
P = m*g

# Força Elástica
k = 10000                   # Constante da 'Mola'
x0 = 1                      # Valor inicial x da Mola
y0 = 1                      # Valor inicial y da Mola

# Força de Atrito
u = 0.5                         # Coeficiente de atrito
N = m*g                         # Normal = Peso (plano reto)
Fat = u*N                       



#Resolução Odeint
Vox = 11.4623138919
Voy =  -57.287922142
tempoI1 = np.arange(0,0.035,0.000001)         # Tempo de Durção do 1 Salto
I0 = [x0,Vox,y0,Voy]                      # Condições Iniciais
Imp1 = odeint(Impulso,I0,tempoI1)     # Resolução Odeint
V = []
for i in range(len(tempoI1)):
        V.append((Imp1[i,1]**2 + Imp1[i,3]**2)**0.5)

print(Imp1[:,1][-1],Imp1[:,3][-1],Imp1[:,0][-1],Imp1[:,2][-1])

plt.plot(tempoI1,V)
plt.xlabel("tempo")
plt.ylabel("V")
plt.title("V por tempo")
plt.show()
        
plt.plot(Imp1[:,0],Imp1[:,2],)
plt.xlabel("x")
plt.ylabel("Y")
plt.title("x por y")
plt.show()

plt.plot(tempoI1,Imp1[:,0],)
plt.xlabel("Tempo")
plt.ylabel("varição de x")
plt.title("x por tempo")
plt.show()


plt.plot(tempoI1,Imp1[:,1],)
plt.xlabel("Tempo")
plt.ylabel("Variação Vx")
plt.title("Vx por tempo")
plt.show()

plt.plot(tempoI1,Imp1[:,2],)
plt.xlabel("Tempo")
plt.ylabel("varição de y")
plt.title("y por tempo")
plt.show()


plt.plot(tempoI1,Imp1[:,3],)
plt.xlabel("Tempo")
plt.ylabel("Variação Vy")
plt.title("Vy por tempo")
plt.show()



