import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import logging
import json
from typing import List, Optional
from pydantic import BaseModel, ValidationError, Field


class Coeff(BaseModel):
    beta: float = Field(alias="intensity_of_contacts")
    gamma: float = Field(alias="recovery_rate")
    N: float = Field(alias="base_normalization")
    h: float = Field(alias="step_in_days")
    S0: float = Field(alias="susceptible_individuals_initial")
    I0: float = Field(alias="infected_individuals_initial")
    R0: float = Field(alias="ill_individuals_initial")
    day: float


logging.basicConfig(filename="app.log", level=logging.INFO)


def ReadConfig(Name) -> np.ndarray:
    logging.info("Trying to open the file")
    file = open(Name, "r")
    data = file.read()
    try:
        C = Coeff.parse_raw(data)
    except ValidationError as e:
        print("Exception", e.json())
    coeff = np.array([C.beta, C.gamma, C.N, C.h, C.S0, C.I0, C.R0, C.day])
    return coeff


# funtion S'
def dS_dt(S: float, I: float) -> float:
    total = -(beta * I * S) / N
    return total


# funtion I'
def dI_dt(I: float, S: float) -> float:
    total = beta * I * S / N - gamma * I
    return total


# funtion R'
def dR_dt(I: float) -> float:
    total = gamma * I
    return total


# RK:S , I ,R
def rungeKutta(RK: np.ndarray) -> np.ndarray:

    S, I, R = RK[0], RK[1], RK[2]
    k1S = h * dS_dt(S, I)
    k1I = h * dI_dt(I, S)
    k1R = h * dR_dt(I)

    k2S = h * dS_dt(S + k1S / 2, I + k1I / 2)
    k2I = h * dI_dt(I + k1I / 2, S + k1S / 2)
    k2R = h * dR_dt(I + k1I / 2)

    k3S = h * dS_dt(S + k2S / 2, I + k2I / 2)
    k3I = h * dI_dt(I + k2I / 2, S + k2S / 2)
    k3R = h * dR_dt(I + k2I / 2)

    k4S = h * dS_dt(S + k3S / 2, I + k3I / 2)
    k4I = h * dI_dt(I + k3I / 2, S + k3S / 2)
    k4R = h * dR_dt(I + k3I / 2)

    S1 = S + (k1S + k2S * 2 + k3S * 2 + k4S) / 6
    I1 = I + (k1I + k2I * 2 + k3I * 2 + k4I) / 6
    R1 = R + (k1R + k2R * 2 + k3R * 2 + k4R) / 6

    Next = np.array([S1, I1, R1])

    return Next


# RK= S0 , I0 ,R0
# Funtion solution
def solution(RK: np.ndarray, day: float) -> np.ndarray:
    count = 0

    S = np.array([RK[0]])
    I = np.array([RK[1]])
    R = np.array([RK[2]])
    T = np.array(0)
    while count < day:
        Next = rungeKutta(RK)

        S = np.append(S, Next[0])
        I = np.append(I, Next[1])
        R = np.append(R, Next[2])

        RK = Next

        count = count + h
        T = np.append(T, count)

    sol = np.array([S, I, R, T])

    return sol


coeff: np.ndarray = ReadConfig("Config.json")
[beta, gamma, N, h] = coeff[0:4]
sol = solution(coeff[4:7], coeff[7])


def main():
    plt.plot(sol[3], sol[0], label="the number of susceptible individuals at time t")
    plt.plot(sol[3], sol[1], label="the number of infected individuals at time t")
    plt.plot(sol[3], sol[2], label="the number of ill individuals at time t")
    plt.show()


if __name__ == "__main__":
    main()
