from math import log, sqrt, exp
from numpy import zeros
from scipy.stats import norm

def Black_Scholes_call(S, K, T, r, sigma, t):
    C = zeros(len(S))
    P = zeros(len(S))
    for i in range(len(S)):
        d1 = (log(S[i]/K) + (r + 0.5*sigma**2)*(T-t))/(sigma*sqrt(T-t))
        d2 = d1 - sigma*sqrt(T-t)
        N1 = norm.cdf(d1)
        N2 = norm.cdf(d2)
        C[i] = S[i]*N1 - K*exp(-r*(T-t))*N2
        P[i] = K*exp(-r*(T-t))*(1-N2) - S[i]*(1-N1)
    return C

# def Black_Scholes_call_3d(S, K, T, r, sigma, t):
#     C = zeros(len(S))
#     P = zeros(len(S))

#     d1 = (log(S/K) + (r + 0.5*sigma**2)*(T-t))/(sigma*sqrt(T-t))
#     d2 = d1 - sigma*sqrt(T-t[i])
#     N1 = norm.cdf(d1)
#     N2 = norm.cdf(d2)
#     C = S*N1 - K*exp(-r*(T-t))*N2
#     P = K*exp(-r*(T-t))*(1-N2) - S*(1-N1)
#     return C