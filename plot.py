import numpy as np
import matplotlib.pyplot as plt

a=0
b=10
n=6
x=[0, 1, 4, 5,  7, 10]
f=[1, 2, 5, 8, 11, 12]
d=[1, 3, 2, 4,  5,  1]
print(list(range(n)))
print(x)
print("*************************************")

def bin_debug(t,x):
    print("---------------------------------------")
    print(f"Printing bin({t},x)")

    n=len(x)
    start=0
    fin=n-1
    mid=n//2
    #print(f"{start=}")
    #print(f"{fin=}")
    #print(f"{mid=}")
    for index, i in enumerate(x):
        if(t==i):
            return index
    while(True):
        #print("...loop")
        if(t<=x[mid]):
            #print("   t<=x[mid]")
            #print(f"   {mid=}")
            #print(f"   {x[mid]=}")
            fin=mid+1
            x=x[start:fin]
            #print(f"   {x=}")
            if(len(x)<=2):
                return start
            mid=(fin-start)//2

            #print(f"   {start=}")
            #print(f"   {fin=}")
            #print(f"   {mid=}")
        else:
            #print("   t>x[mid]")
            #print(f"   {mid=}")
            #print(f"   {x[mid]=}")
            start=start+mid
            x=x[start:fin+1]
            #print(f"   {x=}")
            if(len(x)<=2):
                return start
            mid=(fin-start)//2
            #print(f"   {start=}")
            #print(f"    {fin=}")
            #print(f"    {mid=}")

def bin(t,x):
    print(f"Printing bin({t},x)")

    n=len(x)
    start=0
    fin=n-1
    mid=n//2
    for index, i in enumerate(x):
        if(t==i):
            return index
    while(True):
        if(t<=x[mid]):
            fin=mid+1
            x=x[start:fin]
            if(len(x)<=2):
                return start
            mid=(fin-start)//2
        else:
            start=start+mid
            x=x[start:fin+1]
            if(len(x)<=2):
                return start
            mid=(fin-start)//2

#print(f"{bin(0,x)=}")
#print(f"{bin(8,x)=}")
#print(f"{bin(1,x)=}")
#print(f"{bin(2,x)=}")
#print(f"{bin(3,x)=}")
#print(f"{bin(4.5,x)=}")
#print(f"{bin(6,x)=}")
#print(f"{bin(7,x)=}")
#print(f"{bin(9,x)=}")
#print(f"{bin(10,x)=}")


# provide a,b,n also
def rqs(t,x,f,d):
    # calculate h and delta
    h=[]
    for i in range(5):
        h.append(x[i+1]-x[i])
    print(f"{h=}")

    delta=[]
    for i in range(5):
        delta.append( (f[i+1]-f[i])/h[i])
    print(f"{delta=}")
    # determine which bin (i) t belongs to
    i=bin(t,x)
    # calculate theta(t)
    theta=(t-x[i])/h[i]
    print(f"{theta=}")
    # caluclate P(theta)
    P=(delta[i]*f[i+1]*theta*theta+
        (f[i]*d[i+1]+f[i+1]*d[i])*theta*(1-theta)
        +delta[i]*f[i]*(1-theta)*(1-theta)
        )
    print(f"{P=}")
    # calculate Q(theta)
    Q=delta[i]+(d[i+1]+d[i]-2*delta[i])*theta*(1-theta)
    print(f"{Q=}")
    # return P/Q
    if(Q!=0):
        print(f"{(P/Q)=}")
        return P/Q
    else:
        return 0

rqs(2.5,x,f,d)


dx=(b-a)/1000
t=np.arange(a,b,dx)
rq=np.array([rqs(tt,x,f,d) for tt in t])
print(t)
print(rq)

plt.scatter(x,f, c="r")
plt.plot(t,rq)
plt.show()
