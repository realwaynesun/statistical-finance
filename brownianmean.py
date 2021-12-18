import math

def mandv(fy,mu1,sigma1,sy,mu2,sigma2,initial):
    mu=fy*mu1+sy*mu2+initial
    v=fy*sigma1**2+sy*sigma2**2
    return mu,v

result=mandv(2, 7, 3, 4, 3, 5, 10)
print(result)