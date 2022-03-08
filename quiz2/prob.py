import scipy.stats as stats
import numpy as np
import math
from sympy import *

#after x months the mean and the variance of the cash position;
def msv(drift,variance,initial,time):
    m=drift*time+initial
    v=variance*time
    s=math.sqrt(v)
    i=initial
    return m,v,s,i

#the probability of a negative cash position at the end of x months;
def pro(mu,sigma):
    probability_cdf = stats.norm.cdf(-(mu/sigma),0,1)
    return probability_cdf

#have a less than x% chance of a negative cash position by the end of x months;
#beware the initial in paramaters is the initial position given by quiz;
def inipos(sigma,mu,initial):
    ppf=stats.norm.ppf(0.05,0,1)
    m=mu-initial
    x=-ppf*sigma-m
    return x

mu,var,sigma,initial=msv(0.01, 0.14, 0.05, 10)
p=pro(mu, sigma)
ini=inipos(sigma, mu, initial)
print("\n")
print("The mean and the variance of the cash position are " + str(mu) + ", " + str(var) + ".\n")
print("The probability is " + str(p) + ".\n")
print("The initial position is " + str(ini) + ".\n")
