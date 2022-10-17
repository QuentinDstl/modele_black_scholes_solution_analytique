from math import log, sqrt, exp
from numpy import zeros
from scipy.stats import norm

def Black_Scholes_call(S, K, T, r, sigma):
    C = zeros(len(S))
    P = zeros(len(S))
    for i in range(len(S)):
        d1 = (log(S[i]/K) + (r + sigma**2/2)*T)/(sigma*sqrt(T))
        d2 = d1 - sigma*sqrt(T)
        N1 = norm.cdf(d1)
        N2 = norm.cdf(d2)
        C[i] = S[i]*N1 - K*exp(-r*T)*N2
        P[i] = K*exp(-r*(T))*N2 - S[i]*N1
    return C