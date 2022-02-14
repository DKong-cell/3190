import numpy as np
import matplotlib.pyplot as plt
np.seterr(divide='ignore')



class Get_constants():
    
    def __init__(self,L):
        self.L=L
        
    #linear functions
    def Linear_Function(self,a,c):
        y=lambda x:a*x+c
        h=y(self.L)
        return h
    
    def get_spring_constant(self):
        a=3.33
        c=10**(-6)
        k=self.Linear_Function(a,c)
        return k

    def get_width(self):
        a=6.666*(10**(-3))
        c=0.0001
        return self.Linear_Function(a,c)

    def get_thickness(self):
        a=(-6.666*(10**(-3)))
        c=(0.0003)
        return self.Linear_Function(a,c)
    
    def get_density(self):
        a=33333.33
        c=1500
        return self.Linear_Function(a,c)

    def get_mass(self):
        th=self.get_thickness()
        w=self.get_width()
        den=self.get_density()
        V=th*w*self.L
        m=den*V
        return m
    
    
class Amplitude(Get_constants):
    
    def __init__(self,L,frequency_m,F,b):
        super().__init__(L)
        self.k=self.get_spring_constant()
        self.width=self.get_width()
        self.thickness=self.get_thickness()
        self.density=self.get_density()
        self.mass=self.get_mass()
        self.frequency_m=frequency_m
        self.b=b
        self.F=F
        
    #oppgave a
    def frequency(self):
        k=self.k
        m=self.mass
        return (1/(2*np.pi))*np.sqrt(k/m)


    def omega(self):
        k=self.k
        m=self.mass
        return np.sqrt(k/m)

    def omegaF(self):
        return 2*np.pi*self.frequency_m

    def amplitude(self):
        b=self.b
        F=self.F
        m=self.mass
        omega=self.omega()
        omegaF=self.omegaF()
        
        s=0
        A=(F/m)/(np.sqrt((omega**2-omegaF**2)**2 + (b*omegaF/m)**2))
        return A
     
    def Q(self):
        k,b,m=self.k,self.b,self.mass
        return sum((np.sqrt((k*m)/b**2)))
    

L=np.linspace(0,0.03,1000)
c4=261.63
c4_sharp=277.18
F=1
b=1*10**(-3)
#create objects
amplitude_c4=Amplitude(L,c4,F,b)
amplitude_c4_sharp=Amplitude(L,c4_sharp,F,b)
#calculate amplitude
A_c4=amplitude_c4.amplitude()
A_c4_sharp=amplitude_c4_sharp.amplitude()
f=amplitude_c4.frequency()
Q=amplitude_c4.Q()
print(Q)
#plot
#plt.plot(L,f)
plt.plot(L,A_c4,label="C-frequency=261.63HZ")
plt.plot(L,A_c4_sharp,label="C#-frequency=277.18HZ")
plt.ylabel("Amplitude")
plt.xlabel("Length Meter")
plt.legend()
plt.grid(True)
plt.show() 