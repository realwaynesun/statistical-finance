## import certain packages
import math
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sympy import *

S, t, T ,y= symbols('S t T y', real=True)
# 1.type the right function
f = exp(0.01*(T-t))/S

def inver(f,X,Y):
    finv = solve(Y-f,X)
    return finv


def ito(f,mu,sigma,finv):
    
    DS, Dt = map(lambda var: (lambda fcn: diff(fcn, var)), [S, t])
    diffusion_new = DS(f)*sigma*S
    drift_new     = Dt(f) + DS(f)*mu*S + 0.5*DS(DS(f))*(sigma**2)*(S**2)
    drift, diffusion = map(lambda fcn: fcn.subs(S,finv).simplify(),
                                   [drift_new, diffusion_new])
    
    return drift, diffusion


# 2.select the right inverse function;
# 3.input the value of mu and sigma;


finv = inver(f, S, y)
print(finv)
result = ito(f, 0.2, 0.15, finv[0])
print(result)


