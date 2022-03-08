## import certain packages
import math
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sympy import *

S, t, T ,y, r= symbols('S t T y r', real=True)
a = 0.3*(0.09-r)
b = 0.02*sqrt(r)
f = 2*r
def inver(f,X,Y):
    finv = solve(Y-f,X)

    return finv



def itor(a,b,f,finv):
    DS, Dt = map(lambda var: (lambda fcn: diff(fcn, var)), [r, t])
    diffusion_new = DS(f)*b
    drift_new     = Dt(f) + DS(f)*a + 0.5*DS(DS(f))*b**2
    drift, diffusion = map(lambda fcn: fcn.subs(r,finv).simplify(),
                                    [drift_new, diffusion_new])
    return drift, diffusion

finv=inver(f, r, y)
print(finv)
finv=finv[0]
result = itor(a, b, f, finv)
#write down the result on paper for confirmation;
print(result)