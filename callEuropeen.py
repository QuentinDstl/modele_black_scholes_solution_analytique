from math import log, sqrt, exp
from scipy.stats import norm

def callEuropeen(K, T, r, sigma, S0, t):
    d1 = (log(S0/K) + (r + sigma**2/2)*(T-t)) / (sigma*sqrt(T-t))
    d2 = d1 - sigma*sqrt(T-t)
    N1=norm.cdf(-d1)
    N2=norm.cdf(-d2)
    return S0*N1 - K*exp(-r*(T-t))*N2