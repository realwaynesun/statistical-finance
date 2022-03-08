import math
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sympy import *
from scipy.stats import norm

def straddle(r,S,K,t,sigma):
    T=t/12
    d1=(np.log(S/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2=d1-sigma*np.sqrt(T)
    price=S*(norm.cdf(d1, 0, 1)-norm.cdf(-d1, 0, 1)) - K*np.exp(-r*T)*(norm.cdf(d2, 0, 1)-norm.cdf(-d2, 0, 1))
    delta=norm.cdf(d1,0,1)+norm.cdf(d1,0,1)-1
    gamma=2*norm.pdf(d1,0,1)/(S*sigma*np.sqrt(T))
    vega=2*S*norm.pdf(d1, 0, 1)*np.sqrt(T)
    return price,delta,gamma,vega


#This is a straddle option
S=300
K=281
r=0.08
t=3
sigma=0.28


p,d,g,v=straddle(r, S, K, t, sigma)
print("The price is " + str(p) + ".\n")
print("Delta is " + str(d) + ".\n")
print("Gamma is " + str(g) + ".\n")
print("Vega is " + str(v) + ".\n")