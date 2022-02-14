import numpy as np
import matplotlib.pyplot as plt

def log_spring(L):
    return 0.333*np.log(L)+np.log((10**(-6)))

def spring_constant(L):
     
    return 0.333*L+(10**(-6))

def width(L):
    return (-6.666*10**(-4))*L+(0.3*10**(-3))

def thickness(L):
    return (6.666*10**(-4))*L+(0.1*10**(-3))
def density(L):
    return ((3333.33*L)+1500)

def mass(L):
   th=thickness(L)
   w=width(L)
   den=density(L)
   V=th*w*L
   return den*V
def frequency(k,m):
    
    return (1/(2*np.pi))*np.sqrt(k/m)



#length
L=np.linspace(0,0.3,1000)
#spring constant
k=spring_constant(L)
k1=log_spring(L)

#mass in terms of length
m=mass(L)
#frequency
f=frequency(k,m)
f1=frequency(k1,m)



plt.plot(L,f)
plt.grid(True)
plt.xlabel("Length")
plt.ylabel("Frequency")

plt.show()

