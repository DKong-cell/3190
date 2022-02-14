# Note:
#     fineshed with plotting i think . i have to ask the
#     should i take the sum of q factor?
#     is the plot correct?
#     is problem one correct. 
#     what is log ?
#     how to use omega prime


"""
last i did i made a mistake its not 0.3 its 0.03 and check omega with 0.15
"""

import numpy as np
import matplotlib.pyplot as plt
np.seterr(divide='ignore')

def spring_constant(L):
 
    return 3.33*L+(10**(-6))

def width(L):
    return (6.666*(10**(-3)))*L+(0.0001)

def thickness(L):
    return (-6.666*(10**(-3)))*L+(0.0003)
def density(L):
    return ((33333.33*L)+1500)

def mass(L):
   th=thickness(L)
   w=width(L)
   den=density(L)
   V=th*w*L
   return den*V

def frequency(k,m):
    
    return (1/(2*np.pi))*np.sqrt(k/m)


def omega(k,m):
    return np.sqrt(k/m)


def omega_prime(f):
    return f

def amplitude(F,m,omega,omega_prime,b):
    
    return (F/m)/(np.sqrt((omega**2-omega_prime**2)**2 + (b*omega_prime/m)**2))

def ratio(k,m):
    return np.sqrt(k/m)  
def Q(k,b,m):
    return sum((np.sqrt((k*m)/b**2)))
    
    
#constants b=0.1
b=0.0001
F=1
f1=261.63
f2=277.18

# test
L=np.linspace(0,0.03,100)
dens=density(L)
wid=width(L)
thick=thickness(L)
#------------------------------------------------------------------------
k=spring_constant(L)
m=(mass(L))
f=frequency(k,m)
omegas=omega(k,m)
op_1=omega_prime(f1)
op_2=omega_prime(f2)
A1=amplitude(F,m,omegas,op_1,b)
A2=amplitude(F,m,omegas,op_2,b)
ratios=ratio(k,m)
print(Q(k,b,m))
resonace=np.sqrt(omegas**2-op_1**2)

plt.plot(L,A1,label="C-frequency=261.63HZ")
plt.plot(L,A2,label="C#-frequency=277.18HZ")
# plt.xlabel("Length Meter")
plt.ylabel("Amplitude")
plt.legend()
plt.grid(True)
plt.show() 
