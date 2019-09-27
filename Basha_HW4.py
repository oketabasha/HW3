#Homework 4
#worked with Natalia N, Caridad C,Francisko M  
import numpy as np


#Trapezoid Methodimport matplotlip.pyplot as plt
traplist=[]

Om=0.3*(10**3) #Matter density
Or=0.0 #Density of
Oa=0.7 #Density of dark energy
pw=range(1,100)
def tra(z):

    trap=0
    for x in range(0,int(z)):

        Hz=np.sqrt((Om*((1+x)**3))+(Or*((1+x)**2))+Oa)
        trap = trap + ((3e3)/Hz)

    return (trap)/(1 + 10)
#Defining the constants
N=1000
a=0.0
for b in range (1,1):
    h=(b-a)/N
    s=(0.5*tra(a))+(0.5*tra(b))
    print(s)
    
    for k in range(1,N):
        s+=tra(a+(k*h))
    fvl=h*s
    traplist.append(fvl)
    print(h*s)
print("trapezoid method")
print(traplist) 


#using np.trapz
def r(z):
    # Define the constants
    Om = 0.3
    Or = 0.
    Ol = 0.7
    c = 3.e3
    
    return c/np.sqrt((Om)*((1.+z)**3.) + (Or)*((1+z)**2.) + Ol)

def trapz_Da(z):
    da = []

    for i in z:
        d = np.trapz([r(min(z)),r(i+1)])/(1.+i)
        da.append(d)
              
    return np.array(da)

 
#Gaussian Method
from numpy import ones,copy,cos,tan,pi,linspace
gausslist=[]
def gaussxw(N):
    a = linspace(3,4*N-1,N)/(4*N+2)
    x=cos(pi*a+1/(8*N*N*tan(a)))

    elipson=1e-15
    delta=1.0
    while delta>elipson:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 =p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w
print ("Gauss Method")
print (gaussxwab(1000,0,10))


#Linear method
lin=[]
x=range(0,11)
y=lin
b=0
Om=0.3*(10**3) #Matter density
Or=0.0 #Density of
Oa=0.7 #Density of dark energy
def f(z):
    C=3e3
    Hz=np.sqrt(Om*((1+z)**3)+Or*((1+z)**2)+Oa)
    return C/Hz

for z in range(1,11):
    D=((z-b)*f(z))/(1+(z+1))
    lin.append(D)
print("Linear Method")
print(lin)

#Simpson's rule:
sim=[]
N=1000.0
a=0.0
b=10.0
j=0.0
Om=0.3*(10**3) #Matter density
Or=0.0 #Density of
Oa=0.7 #Density of dark energy
def f(z):
    C=3e3
    Hz=np.sqrt(Om*((1+z)**3)+Or*((1+z)**2)+Oa)
    return C/Hz

def simp(r,a,b,N):
    G=(b-a)/float(N)
    x=h+a
    for i in range(1,N,2):
        j+=4*f(z)
        x+=2*G
    x=a+2*G
    for z in range(2,N,2):
            j+=2*f(z)
            x+=2*h
    return (G/3)*(f(a)*f(b)+j)
    for z in range(0,11):
        S=(simp(r,0,z,1000)/(1+z))
        sim.append(S)
print(sim)
    


#plots:
import matplotlib.pyplot as plt
print("Linear Method")
print(lin)

plt.title('Trapezoidal Method')
plt.plot(range(10),traplist)
plt.show()

plt.title('np.trapz')
plt.plot(range(10),np.array(da))
plt.show()

plt.title('Gaussian Method')
plt.plot(range(10),gaussxwab(10,0,10)[0])
plt.show()

plt.title('Linear Method')
plt.plot(range(10),lin)
plt.show()

ply.title('Simpsons Method')
plt.plot(range(10),sim)

#I am well aware that these graphs are not correct, and I wasnt able to see the improvement of the error with diffferent methods, but at least the codes work...
