import math
from datetime import datetime, date
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame

def simplebino(S, K, T, u, d, r, N, Type, AorE):
    # The percentage increase in the stock price when there is an up movement is u-1;
    # The percentage decrease when there is a down movement is 1 - d;
    # The risk-free interest is r per annum;
    # The time to maturity is T years;
    # The probability of an up movement in a risk-neutral world is up;
    # The probability of an down movement in a risk-neutral world is dp;
    # The Number of binomial steps is N; 
    # The underlying stock price is S;
    # The exercise price is K;
    # The type of the option is Type "C" or "P";
    # The American or European options is "A" or "E";

    up = (math.exp(r*T/N)-d)/(u-d)
    dp = 1 - up
    disc=math.exp(-r*T/N)
    print("The risk neutral probability is " + str(up))
    # SP is the list of stock price on final step;
    # CP is the list of option value on each node;
    SP = [0] * (N+1)
    CP = [0] * (N+1)
    
    SP[0]=S*d**N
    L=[]  # The list to store European option value;
    LA=[] # The list to store American option value;
    OP=[] # The list to store option payoffs on the last step;
    for a in range(1, N+1): 
        SP[a] = SP[a-1]*u/d
    for a in range(0, N+1):
        if  Type == 'P':
            CP[a] = max(K-SP[a],0)
            OP.append(CP[a])
        elif Type == 'C':
            CP[a] = max(SP[a]-K,0)
            OP.append(CP[a])
    for b in range(N, 0, -1):
        for a in range(0, b):
            CP[a] = disc*(up*CP[a+1]+dp*CP[a])
            L.append(CP[a])
    if AorE == "E":
        print(L)
        if N==1:
            PD=OP[0]
            PU=OP[1]
            delta=(PU-PD)/(S*(u-d))
            PV=math.exp(-r*T/N)*(S*u*delta-PU)
            print("delta is "+str(delta)+". The present value is "+str(PV)+".")
 

    if AorE == "A":
        # We need to compare the option value and the payoff from early exercise on every node;

        for m in range(1,N+1):
            SPB=[0]*(N-m+1) # We have N-m possible stock prices on step N-m;
            SPB[0]=S*d**(N-m) # The lowest stock price of step N-m;
            for c in range(1, N-m+1):
                SPB[c]=SPB[c-1]*u/d
                if Type == "P":
                    if K-SPB[c-1]-L[c-1]>0:
                        L[c-1]=K-SPB[c-1]
                        
                        print("We should exercise early on step " + str(N-m+1) )

                    else :
                        print( "Early exericse is not optimal.")
                elif Type == "C":
                    if SPB[c-1]-K-L[c-1]>0:
                        L[c-1]=SPB[c-1]-K

                        print("We should exercise early on step " + str(N-m+1) )

                    else:
                        print("Early exericse is not optimal.")
            
                for x in range(N-m,0,-1):
                    for y in range(0,x):
                        L[y]=disc*(up*L[y+1]+dp*L[y])
                        LA.append(L[y])

                print("The American option vallue is "+str(LA))




question1=simplebino(100, 99, 4/12, 1.17, 0.92, 0.05, 2, 'P', 'A')

#example1=simplebino(50, 52, 2, 1.2, 0.8, 0.05, 2, 'P', 'A')


