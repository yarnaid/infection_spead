
from configparser import ConfigParser
from array import *
from scipy import integrate
import matplotlib.pyplot as plt
from math import e
from scipy import integrate as inte
import numpy as np


def ReadConfig(Name):
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
[beta , gamma , N , h , S0 , I0 , R0 , day] = ReadConfig('config.ini')

def SIR_model(t, y ):
    
    
    S, I, R = y
    dS = -(beta * I * S)/N
    dI = beta * I * S / N - gamma * I
    dR = gamma*I
    return [dS,dI, dR]

def solution(S0 , I0 , R0 , day  , h):

    y0 = [S0,I0,R0]
    y1 = SIR_model(0, y0 )
    solution = integrate.RK45(SIR_model, 0, y0 ,day ,h, 0.001, e**-6)
    S = np.array([])
    I = np.array([])
    R = np.array([])
    T = np.array([])
    while (solution.t < day ):
    # get solution step state
      solution.step()
      T = np.append(T , solution.t)
      S = np.append(S , solution.y[0])
      I = np.append(I , solution.y[1])
      R = np.append(R , solution.y[2])
    return [S , I ,R ,T]
    


[S , I ,R ,T] = solution(S0 , I0 , R0 , day , h )
print(solution(S0 , I0 , R0 , day , h ))
plt.plot(T , S ,  label = 'the number of susceptible individuals at time t')
plt.plot(T , I ,  label = 'the number of infected individuals at time t')
plt.plot(T , R ,  label = 'the number of ill individuals at time t')
plt.show()




