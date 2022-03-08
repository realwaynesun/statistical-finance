import math
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from sympy import *
from scipy.stats import norm


def volrho(col11,col12,col13,col22,col23,col33):
    cov12=col12
    cov13=col13
    cov23=col23
    vol1=math.sqrt(col11)
    vol2=math.sqrt(col22)
    vol3=math.sqrt(col33)
    vol=[vol1,vol2,vol3]
    rho12=cov12/(vol1*vol2)
    rho13=cov13/(vol1*vol3)
    rho23=cov23/(vol2*vol3)
    rho=[rho12,rho13,rho23]
    return vol,rho

def twoport(asset1,asset2,vol,rho,number1,number2,n,prob):
    p=norm.ppf(prob)
    sd=math.sqrt((asset1*vol[number1-1])**2+(asset2*vol[number2-1])**2+2*rho[number1+number2-3]*(asset1*vol[number1-1])*(asset2*vol[number2-1]))
    VaR=p*math.sqrt(n)*sd
    VaR1=p*math.sqrt(n)*asset1*vol[number1-1]
    VaR2=p*math.sqrt(n)*asset2*vol[number2-1]
    benefit=VaR1+VaR2-VaR
    return VaR, benefit

def threeport(asset1,asset2,asset3,vol,rho,n,prob):
    p=norm.ppf(prob)
    sd=math.sqrt((asset1*vol[0])**2+(asset2*vol[1])**2+(asset3*vol[2])**2+2*rho[0]*(asset1*vol[0])*(asset2*vol[1])+2*rho[1]*(asset1*vol[0])*(asset3*vol[2])+2*rho[2]*(asset2*vol[1])*(asset3*vol[2]))
    VaR=p*math.sqrt(n)*sd
    VaR1=p*math.sqrt(n)*asset1*vol[0]
    VaR2=p*math.sqrt(n)*asset2*vol[1]
    VaR3=p*math.sqrt(n)*asset2*vol[2]
    benefit=VaR1+VaR2+VaR3-VaR
    return VaR, benefit
    

col11=0.0016
col12=0.00024
col13=-0.00096
col22=0.0004
col23=-0.00024
col33=0.0036
vol,rho=volrho(col11, col12, col13, col22, col23, col33)
#question1
asset1=300
asset2=300
number1=1
number2=2
n=5
prob=0.90
v1,b1=twoport(asset1,asset2,vol,rho,number1,number2,n,prob)
print("Answer of q1 is " + str(v1)+", "+str(b1))
#question2
asset1=300
asset2=300
number1=1
number2=3
n=5
prob=0.90
v2,b2=twoport(asset1,asset2,vol,rho,number1,number2,n,prob)
print("Answer of q2 is " + str(v2)+", "+str(b2))
#question3
asset1=200
asset2=200
asset3=200
v3,b3=threeport(asset1, asset2, asset3, vol, rho, n, prob)
print("Answer of q3 is " + str(v3)+", "+str(b3))
