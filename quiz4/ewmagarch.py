import math
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sympy import *
from scipy.stats import norm

def ewma(sigma0,p0,p1,lamda):
    u=ln(p1/p0)
    s=math.sqrt(lamda*sigma0**2+(1-lamda)*u**2)
    return s

def garch1(omega,alpha,beta,p0,p1,sigma0):
    u=ln(p1/p0)
    s=math.sqrt(omega+alpha*u**2+beta*sigma0**2)
    return s

sigma0=1.7/100 #The daily volatility of the index
p0=28500 #The level of the index yesterday
p1=25000 #The level of the index today
lamda=0.93

s=ewma(sigma0, p0, p1, lamda)

print(s)



omega=2*10**(-6)
alpha=0.05
beta=0.9
s1=garch1(omega, alpha, beta, p0, p1, sigma0)
print(s1)