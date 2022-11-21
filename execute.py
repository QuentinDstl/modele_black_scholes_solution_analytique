from math import log, exp
from numpy import zeros, linspace, meshgrid
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Black_Scholes_call import Black_Scholes_call


## fonction sortie Call 2D ##
def execute(N, K, T, r, sigma):
    L = log(3)
    x = zeros(N)
    S = zeros(N)
    x = linspace(-1,1,N)
    t=0
    for i in range(N):
        S[i] = K*exp(L*x[i])
    C = Black_Scholes_call(S, K, T, r, sigma, t)
    return [S,C]

## fonction sortie Call 3D ##
def execute3d(N, K, T, r, sigma):
    L = log(3)
    x = zeros(N)
    Svals = zeros(N)
    tvals = zeros(N)
    C0 = zeros(N)
    C = zeros((N,N))
    x = linspace(-1,1,N)
    e = 1*exp(-4)
    Svals = linspace(e, 3, N)
    tvals = linspace(e, T-e, N)
    for i in range(N):
        C0 = Black_Scholes_call(Svals, K, T, r, sigma, tvals[i])
        C[i,:] = C0
    return [Svals, tvals, C]

## Sortie 2d ##
[S, C] = execute(200, 100, 1, 0.1, 0.3)
plt.plot(S, C)
plt.plot(S, C)
plt.show()

## sortie Call 3D ##
[Svals, tvals, C] = execute3d(200, 1, 1, 0.1, 0.3)
S, t = meshgrid(Svals, tvals)
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(S, t, C, rstride=1, cstride=1, cmap='viridis', edgecolor='none')
plt.show()


