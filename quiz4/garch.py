import math
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sympy import *
from scipy.stats import norm

def garch(alpha, beta, omega, sigma, delta, T):
    V=omega/(1-alpha-beta)
    vol=math.sqrt(V+(sigma**2-V)*(alpha+beta)**T)
    a=np.log(1/(alpha+beta))
    b=math.sqrt(252)*sigma
    vol_op=math.sqrt(252*(V+(1-exp(-a*T))*(sigma**2-V)/(a*T)))
    new_sigma=sigma+delta
    c=math.sqrt(252)*new_sigma
    new_vol=math.sqrt(V+(new_sigma**2-V)*(alpha+beta)**T)-vol
    new_vol_op=(1-exp(-a*T))/(a*T)*b/vol_op*(c-b)+vol_op
    return vol, vol_op, new_vol, new_vol_op

omega=8*10**(-6)
alpha=0.06
beta=0.89
sigma=1.7/100
T1=20
T2=300
delta=0.1/100

vol1, vol_op1, new_vol1, new_vol_op1=garch(alpha, beta, omega, sigma, delta, T1)
print("Volatility in "+ str(T1) + " days: "+ str(vol1) +" " +str(vol_op1) + " "+str(new_vol1) +" "+ str(new_vol_op1))

vol2,vol_op2,new_vol2, new_vol_op2=garch(alpha, beta, omega, sigma, delta, T2)
print("Volatility in "+ str(T2) + " days: "+ str(vol2) +" " +str(vol_op2) + " "+str(new_vol2) +" "+ str(new_vol_op2))