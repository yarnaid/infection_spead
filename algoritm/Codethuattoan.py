from configparser import ConfigParser
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def ReadConfig(Name) -> "numpy.ndarray":
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

    coeff = np.array([beta, gamma, N, h, S0, I0, R0, day])

    return coeff


# funtion S'
def F1(S: float, I: float) -> float:
    total = -(beta * I * S) / N

    return total


# funtion I'
def F2(I: float, S: float) -> float:
    total = beta * I * S / N - gamma * I
    return total


# funtion R'
def F3(I: float) -> float:
    total = gamma * I
    return total


# RK:S , I ,R
def rungeKutta(RK: "numpy.ndarray") -> "numpy.ndarray":

    [S, I, R] = RK[0:3]
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

    Next = np.array([S1, I1, R1])

    return Next


# RK= S0 , I0 ,R0
# Funtion solution
def solution(RK: "numpy.ndarray", day: float) -> "numpy.ndarray":
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


coeff: "numpy.ndarray" = ReadConfig("config.ini")
[beta, gamma, N, h] = coeff[0:4]
sol = solution(coeff[4:7], coeff[7])


def main():
    plt.plot(sol[3], sol[0], label="the number of susceptible individuals at time t")
    plt.plot(sol[3], sol[1], label="the number of infected individuals at time t")
    plt.plot(sol[3], sol[2], label="the number of ill individuals at time t")
    plt.show()


if __name__ == "__main__":
    main()
