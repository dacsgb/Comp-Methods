import numpy as np

def delta(n,B1,Bn):
    d = np.log(B1/Bn)/n
    return d

def zeta(d):
    z = d/np.sqrt(4*np.pi**2 + d**2)
    return z

def c(z,m,k):
    c = 2*z*np.sqrt(m*k)
    return c

def wn(m,k):
    wn = np.sqrt(k/m)
    return wn

def wd(wn,z):
    wd = wn*np.sqrt(1-z**2)
    return wd

def main():
    n = 4
    B1 = 0.76199
    Bn = 0.1269
    m = 0.61
    k = 70.07+65.4


    delt = delta(n,B1,Bn)
    zet = zeta(delt)
    c1 = c(zet,m,k)
    wn1 = wn(m,k)
    wd1 = wd(wn1,zet)

    print("delta =", delt)
    print("zeta =", zet)
    print("dampening Coefficient =", c1)
    print("natural freq =", wn1)
    print("dampended freq =", wd1)

main()
