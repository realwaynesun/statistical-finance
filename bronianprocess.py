import numpy as np
import math
from sympy import *
import scipy.stats as stats

def dts(initial, time, mu, sigma):
    e=initial*exp(mu*time)
    s=sigma*initial*sqrt(time)
    return e, s

def dtls(initial, time, mu, sigma):
    E=initial*exp(mu*time)
    V=(initial**2)*exp(2*mu*time)*(exp(time*sigma**2)-1)
    SD=sqrt(V)
    return E, SD

def ls(initial, time, mu, sigma):
    LE=np.log(initial)+(mu-(sigma**2)/2)*time
    LV=time*sigma**2
    LSD=sqrt(LV)
    return LE, LSD

def p(value, LE, LSD):
    p = 1-stats.norm.cdf(np.log(value),LE,LSD)
    return p

def conint(LE,LSD,per):
    inter=stats.norm.interval(per,0,1)
    u=exp(LE+inter[1]*LSD)
    d=exp(LE+inter[0]*LSD)
    return [d,u]

initial = 50
time = 1/6
mu = 0.18
sigma = 0.2
value = 55
per = 0.9
e, s = dts(initial, time, mu, sigma)
E, SD = dtls(initial, time, mu, sigma)
LE, LSD = ls(initial, time, mu, sigma)
interval = conint(LE, LSD, per)
p = p(value, LE, LSD)
print("\n")
print("S gives that the mean and the standard deviation are " + str(e) + " and " + str(s) + ".\n")
print("ln(S) yields that the mean and the standard deviation are " + str(E) + " and " + str(SD) + ".\n")
print("The mean and the standard deviation of ln(S_T) are " + str(LE) + " and " + str(LSD) + ".\n")
print("The probability that S_T is greater than " + str(value) + " is " + str(p) + ".\n")
print("The " + str(per) + " confidence interval is " + str(interval) + ".\n")