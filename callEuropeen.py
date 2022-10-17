from math import log, sqrt, exp
from scipy.stats import norm

def callEuropeen(K, T, r, sigma, S0, t):
    d1 = (log(S0/K) + (r + sigma**2/2)*(T-t)) / (sigma*sqrt(T-t))
    d2 = d1 - sigma*sqrt(T-t)
    return K*exp(-r*(T-t))*norm.cdf(-d2) - S0*norm.cdf(-d1)