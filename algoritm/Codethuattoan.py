from configparser import ConfigParser
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


class Coefficient:
    def __init__(self, beta, gamma, N, h, S0, I0, R0, day):
        self.day = day
        self.beta = beta
        self.gamma = gamma
        self.N = N
        self.h = h
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0


class Solution:
    def __init__(self, S, I, R, T):
        self.S = S
        self.I = I
        self.R = R
        self.T = T


class NextrungeKutta:
    def __init__(self, S, I, R):
        self.S = S
        self.I = I
        self.R = R


def ReadConfig(Name):
    config = ConfigParser()

    print(config.sections())
    config.read(Name)

    beta = float(
        config["coefficient"][
            "coefficient of intensity of contacts of individuals with subsequent infection"
        ]
    )
    gamma = float(config["coefficient"]["recovery rate of infected individuals"])
    N = float(config["coefficient"]["base normalization number"])
    h = float(config["coefficient"]["fixed step (days)"])

    S0 = float(
        config["initialcondition"][
            "the number of susceptible individuals at the initial moment of time"
        ]
    )
    I0 = float(
        config["initialcondition"][
            "the number of infected individuals at the initial moment of time"
        ]
    )
    R0 = float(
        config["initialcondition"][
            "the number of ill individuals at the initial moment of time"
        ]
    )

    day = int(config["Days"]["day"])

    coeff = Coefficient(beta, gamma, N, h, S0, I0, R0, day)

    return coeff


# funtion S'
def F1(S, I):
    total = -(beta * I * S) / N

    return total


# funtion I'
def F2(I, S):
    total = beta * I * S / N - gamma * I
    return total


# funtion R'
def F3(I):
    total = gamma * I
    return total


def rungeKutta(S, I, R):
    k1S = h * F1(S, I)
    k1I = h * F2(I, S)
    k1R = h * F3(I)

    k2S = h * F1(S + k1S / 2, I + k1I / 2)
    k2I = h * F2(I + k1I / 2, S + k1S / 2)
    k2R = h * F3(I + k1I / 2)

    k3S = h * F1(S + k2S / 2, I + k2I / 2)
    k3I = h * F2(I + k2I / 2, S + k2S / 2)
    k3R = h * F3(I + k2I / 2)

    k4S = h * F1(S + k3S / 2, I + k3I / 2)
    k4I = h * F2(I + k3I / 2, S + k3S / 2)
    k4R = h * F3(I + k3I / 2)

    S1 = S + (k1S + k2S * 2 + k3S * 2 + k4S) / 6
    I1 = I + (k1I + k2I * 2 + k3I * 2 + k4I) / 6
    R1 = R + (k1R + k2R * 2 + k3R * 2 + k4R) / 6

    Next = NextrungeKutta(S1, I1, R1)

    return Next


# Funtion solution
def solution(day, S0, R0, I0):
    count = 0
    S = [S0]
    I = [I0]
    R = [R0]
    T = [0]
    while count < day:
        Next = rungeKutta(S0, I0, R0)

        S.append(Next.S)
        I.append(Next.I)
        R.append(Next.R)

        S0, I0, R0 = Next.S, Next.I, Next.R
        count = count + h
        T.append(count)

    sol = Solution(S, I, R, T)

    return sol


coeff = ReadConfig("config.ini")
[beta, gamma, N, h] = [coeff.beta, coeff.gamma, coeff.N, coeff.h]

sol = solution(coeff.day, coeff.S0, coeff.R0, coeff.I0)


def main():
    plt.plot(sol.T, sol.S, label="the number of susceptible individuals at time t")
    plt.plot(sol.T, sol.I, label="the number of infected individuals at time t")
    plt.plot(sol.T, sol.R, label="the number of ill individuals at time t")
    plt.show()


if __name__ == "__main__":
    main()
