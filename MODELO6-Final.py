#MODELO HULK 3 

import math
from scipy.integrate import odeint
import numpy as np
import matplotlib.pyplot as plt
d = 0
I = 0
while d < 6300000:
        def Impulso(I1,t):
                Qx = I1[0]
                Qy = I1[1]
                dQxdt = FRx 
                dQydt = FRy
               
                return[dQxdt,dQydt]

        def EqDif (A,t):
                x = A[0]
                Vx = A[1]
                y = A[2]
                Vy = A[3]
                dxdt = Vx
                dvxdt = -k*(Vx**2)/m
                dydt = Vy
                dvydt = -(P + k*(Vy**2))/m
                
                return[dxdt,dvxdt,dydt,dvydt]

        def Impulso2(I2,tempoI2):
                Qx = I2[0]
                Qy = I2[1]
                dQxdt = FRx2 
                dQydt = FRy2

                return[dQxdt,dQydt]

        # Condições para o Movimento
        tempoI1 = 0                     # Tempo de Duração de 1 Salto
        tempo = np.arange(0,19.8,0.01)  # Tempo de Duração do 1 Salto
        tempoI2 = np.arange(0,1,0.01)   # Tempo de Duração do 1 Salto


                          
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
        d = 100                                # distância percorrida correndo (V0 = 0)
        Vfat = ((2*d*(Fmuscular-Fat))/m)**0.5  # Velocidade final chegada com o atrito

        # Forças Resultantes xy
        FRy = M + Felpy                 # Impulso1 em y
        FRy2 = M + Felpy - P            # Impulso2 em y
        V0y = FRy*deltaT/m              # velocidade inicial em y

        FRx =(M - Felpx - Fat)          # Impulso1 em x
        FRx2 =(M - Felpx - Fat)         # Impulso2 em x
        V0x = ((FRx)*deltaT + m*Vfat)/m # velocidade inicial em x

        # Força resistencia ar 
        dar = 1.2                       # Densidade do ar
        Ahulk = 6                       # Área do Hulk (Retângulo: 2x3)
        Cd = 0.75                       # Coeficiente de arrasto
        k = 0.5*Cd*Ahulk*1.2            # Constante simplificada ar



        #ODEINT TOTAL

        #Resolução Odeint Impulso Inicial
        
        while I == 0:
                tempoI1 = np.arange(0,1,0.01)            # Tempo de Durção do 1 Salto
                i10 = [m*Vfat,0]                         # Condições Iniciais
                Imp1 = odeint(Impulso,i10,tempoI1)       # Resolução Odeint

                plt.plot(tempoI1,Imp1[:,0],)
                plt.xlabel("Tempo")
                plt.ylabel("Quantiadde de Movimento em x")
                plt.title("IMPULSO INICIAL X")
                plt.show()


                plt.plot(tempoI1,Imp1[:,1],)
                plt.xlabel("Tempo")
                plt.ylabel("Quantiadde de Movimento em y")
                plt.title("IMPULSO INICIAL Y")
                plt.show()
                break
        I += 1
        
                

        
        #Resolução Odeint MOVIMENTO NO LANÇAMENTO

        a0 = [0,V0x,0,V0y]              # Condições Iniciais
        Sol = odeint(EqDif,a0,tempo)    # Resolução Odeint

        plt.plot(tempo,Sol[:,0],)
        plt.xlabel("Tempo")
        plt.ylabel("distância")
        plt.title("Distância máxima por tempo")
        plt.show()
        

        plt.plot(tempo,Sol[:,1],)
        plt.xlabel("Tempo")
        plt.ylabel("Velocidade em x")
        plt.title("Velocidade em x por tempo")

        plt.plot(tempo,Sol[:,2],)
        plt.xlabel("Tempo")
        plt.ylabel("altura")
        plt.title("Altura máxima por tempo")
        plt.show()

        plt.plot(tempo,Sol[:,3],)
        plt.xlabel("Tempo")
        plt.ylabel("Velocidade em y")
        plt.title("Velocidade em y por tempo")
        plt.show()

        #Resolução Odeint Impulso Final
        Varx =  Sol[:,1][-1]               # Velocidade final ar x
        Vary =  Sol[:,3][-1]               # Velocidade final ar y      

        i20 = [Varx,Vary]                  # Condições Iniciais
        Imp2 = odeint(Impulso2,i20,tempoI2) # Resolução Odeint

        plt.plot(tempoI2,Imp2[:,0],)
        plt.xlabel("Tempo")
        plt.ylabel("Quantidade de Movimento em x")
        plt.title("MPULSO FINAL X")
        plt.show()

        plt.plot(tempoI2,Imp2[:,1],)
        plt.xlabel("Tempo")
        plt.ylabel("Quantidade de Movimento em y")
        plt.title("IMPULSO FINAL Y")
        plt.show()
        plt.show()

        
        
        print(d,I)
