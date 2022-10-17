from math import log, sqrt, exp
from numpy import zeros,array,dot,linspace
import matplotlib.pyplot as plt
from Black_Scholes_call import Black_Scholes_call
from scipy.stats import norm

def execute(N, K, T, r, sigma, L):
    L = log(3)
    x = zeros(N)
    S = zeros(N)
    x = linspace(-1,1,N)
    for i in range(N):
        S = K*exp(L*x[i])
    C = Black_Scholes_call(S, K, T, r, sigma,)
    plt.plot(S, C)
    return C


C = execute(200, 100, 1, 0.1, 0.3,)