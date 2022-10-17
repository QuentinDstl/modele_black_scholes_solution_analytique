function Call = Block_Scholes_call()
d1 = (log(S/K)+(r+sigma^2/2)*T)/(sigma*sqrt(T));
d2 = d1-sigma*sqrt(T);
N1 = normcdf(d1);
N2= normcdf(d2);
Call=S*N1-K*exp(-r*T)*N2;


def black_scholes (n)

U0= 15;
Nz= 500;
dz = 0.25;
Nt=5000;
Dt= (365*24*60*60)/Nt;
U1=0;

for i in range(n):
    




