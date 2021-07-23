from configparser import ConfigParser
from array import *
from scipy import integrate
import matplotlib.pyplot as plt



def ReadConfig(Name ):
    config = ConfigParser()

    print(config.sections())
    config.read(Name)

    beta = (float)(config['coefficient']['beta'])
    gamma = (float)(config['coefficient']['gamma'])
    N = (float)(config['coefficient']['N'])
    h = (float)(config['coefficient']['h'])


    S0 = (float)(config['initialcondition']['S0'])
    I0 = (float)(config['initialcondition']['I0'])
    R0 = (float)(config['initialcondition']['R0'])


    day = (int)(config['Days']['day'])

    return [beta , gamma , N , h , S0 , I0 , R0 , day]




def F1(S , I ):
    total = -(beta * I * S)/N
    
    return total

def F2(I , S):
    total = beta * I * S / N - gamma * I
    return total

def F3(I):
    total = gamma * I
    return total

def rungeKutta(S , I , R ):
    k1S = h * F1(S , I)
    k1I = h * F2(I , S)
    k1R = h * F3(I)

    k2S = h * F1(S + k1S/2 , I + k1I/2)
    k2I = h * F2(I + k1I/2 , S + k1S/2)
    k2R = h * F3(I + k1I/2)

    k3S = h * F1(S + k2S/2 , I + k2I/2)
    k3I = h * F2(I + k2I/2 , S + k2S/2)
    k3R = h * F3(I + k2I/2)

    k4S = h * F1(S + k3S/2 , I + k3I/2)
    k4I = h * F2(I + k3I/2 , S + k3S/2)
    k4R = h * F3(I + k3I/2)

    S1 = S + (k1S + k2S * 2 + k3S * 2 + k4S) / 6
    I1 = I + (k1I + k2I * 2 + k3I * 2 + k4I) / 6
    R1 = R + (k1R + k2R * 2 + k3R * 2 + k4R) / 6


    return [S1 , I1 , R1]



   

def solution(day , h , S0 , R0 , I0):
    count = 0
    S = [S0]
    I = [I0]
    R = [R0]
    T = [0]
    while (count < day):
        [S1 , I1 , R1] = rungeKutta(S0 , I0 , R0)

        S.append(S1)
        I.append(I1)
        R.append(R1)

        S0 , I0 , R0 = S1 , I1 , R1
        count  = count + h
        T.append(count)


    return [S ,I , R ,T]


[beta , gamma , N , h , S0 , I0 , R0 , day] = ReadConfig('config.ini')


[S ,I,R ,T] = solution (day , h , S0 , R0 , I0)





plt.plot(T , S ,  label = 'the number of susceptible individuals at time t')
plt.plot(T , I ,  label = 'the number of infected individuals at time t')
plt.plot(T , R ,  label = 'the number of ill individuals at time t')
plt.show()


















    