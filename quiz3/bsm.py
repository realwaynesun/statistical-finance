import math
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sympy import *
from scipy.stats import norm

def blackscholes(r,S,K,t,sigma,Type):
    T=t/12
    d1=(np.log(S/K)+(r+sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2=d1-sigma*np.sqrt(T)
    if Type == "c":
        price = S*norm.cdf(d1, 0, 1) - K*np.exp(-r*T)*norm.cdf(d2, 0, 1)
        delta = norm.cdf(d1, 0, 1)
        probability = norm.cdf(d2,0,1)
    if Type == "p":
        price = K*np.exp(-r*T)*norm.cdf(-d2, 0, 1) - S*norm.cdf(-d1, 0, 1)
        delta = -norm.cdf(-d1, 0, 1)
        probability = norm.cdf(-d2,0,1)
    gamma = norm.pdf(d1, 0, 1)/(S*sigma*np.sqrt(T))
    vega = S*norm.pdf(d1, 0, 1)*np.sqrt(T)
    return price, probability, delta, gamma, vega

Type="c"
S=300
K=247
r=0.02
t=4
sigma=0.18


p,pb,d,g,v=blackscholes(r, S, K, t, sigma, Type)
print("The price is " + str(p) + ".\n")
print("The probability is " + str(pb) + ".\n")
print("Delta is " + str(d) + ".\n")
print("Gamma is " + str(g) + ".\n")
print("Vega is " + str(v) + ".\n")
