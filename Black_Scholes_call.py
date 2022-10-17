from math import log, sqrt, exp
from scipy.stats import norm

def Black_Scholes_call(S, K, T, r, sigma):
    for i in range(len(S)):
        d1 = (log(S[i]/K) + (r + sigma**2/2)*T)/(sigma*sqrt(T))
        d2 = d1 - sigma*sqrt(T)
        C = S[i]*norm.cdf(d1) - K*exp(-r*T)*norm.cdf(d2)
    #P = K*exp(-r*(T-t))*N2 - S*N1
    return C