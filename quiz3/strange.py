import math
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sympy import *
from scipy.stats import norm

def strange(r,S,t,sigma,n1,n2):
    T=t/12
    n=n1-n2
    h=exp((0.5*(sigma**2)*n1*(n1-1)+r*(n1-1))*T)
    price=h*S**n
    delta=n*S**(n-1)*h
    gamma=h*n*(n-1)*S**(n-2)
    vega=n1*(n1-1)*T*sigma*h*S**n
    return price,delta,gamma,vega

n1=6
n2=4
S=2
r=0.02
t=10
sigma=0.25


p,d,g,v=strange(r, S, t, sigma, n1, n2)

print("The price is " + str(p) + ".\n")
print("Delta is " + str(d) + ".\n")
print("Gamma is " + str(g) + ".\n")
print("Vega is " + str(v) + ".\n")