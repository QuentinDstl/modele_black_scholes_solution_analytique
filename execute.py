from math import log, exp
from numpy import zeros, linspace
import matplotlib.pyplot as plt
from Black_Scholes_call import Black_Scholes_call

def execute(N, K, T, r, sigma):
    L = log(3)
    x = zeros(N)
    S = zeros(N)
    x = linspace(-1,1,N)
    for i in range(N):
        S[i] = K*exp(L*x[i])
    C = Black_Scholes_call(S, K, T, r, sigma)
    return [S,C]


[S, C] = execute(200, 100, 1, 0.1, 0.3)
plt.plot(S, C)
plt.show()