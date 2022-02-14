import numpy as np
import matplotlib.pyplot as plt
np.seterr(divide='ignore')

def spring_constant(L):
 
    return 3.33*L+(10**(-6))

def width(L):
    return 66*10**(-4)*L+10**(-4)

def thickness(L):
    return -(66*10**(-4)*L)+10**(-4)
def density(L):
    return (1000/0.03)*L+1500

def mass(L):
   #mass=p*Volume=p*(width*thickness*L)
   return density(L)*(width(L)*thickness(L)*L)

def frequency(k,m):
    
    return (1/(2*np.pi))*np.sqrt(k/m)


def omega(k,m):
    return np.sqrt(k/m)

def omega_prime(omega,b,m):
    gamma = b/2/m
   
    return np.sqrt(gamma**2-omega**2)



def amplitude(F,m,omega,omega_prime,b):
    gamma = b/2/m
    return (F/m)/np.sqrt((omega**2-omega_prime**2)**2 + (2*gamma*omega_prime)**2)
    
  
#constants
b=0.01
F=1
# test
L=np.linspace(0,0.03,10)
dens,wid,thick=[density(L),width(L),thickness(L)]
#variables

k=spring_constant(L)
m=abs(mass(L))
f=frequency(k,m)
omega=omega(k,m)
omega_prime=omega_prime(omega,b,m)

A=amplitude(F,m,omega,omega_prime,b)
plt.plot(L,A)
plt.grid(True)
plt.show() 

# plt.plot(omega_prime/omega,A/(F/m))
# plt.grid(True)
# plt.xlabel("Length")
# plt.ylabel("Frequency")
# plt.show()     