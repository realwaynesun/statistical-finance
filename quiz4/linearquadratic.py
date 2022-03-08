import math
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sympy import *
from scipy.stats import norm

def call(r,S_c,K_c,t_c,sigma_c):
    T=t_c/12
    d1=(np.log(S_c/K_c)+(r+sigma_c**2/2)*T)/(sigma_c*np.sqrt(T))
    d2=d1-sigma_c*np.sqrt(T)
    price = S_c*norm.cdf(d1, 0, 1) - K_c*np.exp(-r*T)*norm.cdf(d2, 0, 1)
    delta = norm.cdf(d1, 0, 1)
    gamma = norm.pdf(d1, 0, 1)/(S_c*sigma_c*np.sqrt(T))    
    return -delta, -gamma

def put(r,S_p,K_p,t_p,sigma_p):
    T=t_p/12
    d1=(np.log(S_p/K_p)+(r+sigma_p**2/2)*T)/(sigma_p*np.sqrt(T))
    d2=d1-sigma_p*np.sqrt(T)
    price = K_p*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S_p*norm.cdf(-d1, 0, 1)
    delta = -norm.cdf(-d1, 0, 1)
    gamma = norm.pdf(d1, 0, 1)/(S_p*sigma_p*np.sqrt(T))
    return -delta, -gamma

def linear(S_c,S_p,delta_c,delta_p,sigma_c,sigma_p,corr,prob,n):
    sigma_c_day=sigma_c/math.sqrt(252)
    sigma_p_day=sigma_p/math.sqrt(252)
    sd_c=delta_c*S_c*sigma_c_day
    sd_p=delta_p*S_p*sigma_p_day
    sd=math.sqrt(sd_c**2+sd_p**2+2*abs(sd_c)*abs(sd_p)*corr)
    p=norm.ppf(prob)
    var=sd*p*math.sqrt(n)
    return abs(sd_c),abs(sd_p),var

def quadratic(S_c,S_p,delta_c,delta_p,sigma_c,sigma_p,gamma_c,gamma_p):
    sigma_c_day=sigma_c/math.sqrt(252)
    sigma_p_day=sigma_p/math.sqrt(252)
    a=1/2*(gamma_c*(sigma_c_day**2)*(S_c**2))**2
    b=1/2*(gamma_p*(sigma_p_day**2)*(S_p**2))**2
    sd_c=math.sqrt((delta_c*S_c*sigma_c_day)**2+a)
    sd_p=math.sqrt((delta_p*S_p*sigma_p_day)**2+b)
    return abs(sd_c),abs(sd_p)

r=0.07
S_c=200
K_c=198
sigma_c=0.15
t_c=7
S_p=300
K_p=323
sigma_p=0.2
t_p=4
corr=-0.1
prob=0.90
n=10
delta_c,gamma_c=call(r, S_c, K_c, t_c, sigma_c)
delta_p,gamma_p=put(r, S_p, K_p, t_p, sigma_p)
a,b,var=linear(S_c, S_p, delta_c, delta_p, sigma_c, sigma_p, corr, prob, n)
sd_c,sd_p=quadratic(S_c, S_p, delta_c, delta_p, sigma_c, sigma_p, gamma_c, gamma_p)
print("Answer of q1 is " + str(a) + ", " + str(b) + ", " + str(var))
print("Answer of q2 is " + str(sd_c) + ", " + str(sd_p))