import numpy as np

y1=0.3/1000
y2=0.1/1000
l1=0/1000
l2=30/1000

m=(y2-y1)/(l2-l1)

x11=m*(-l1)
gg=x11+y1


#print(f"a={m},a*-l1= {x11} , b={gg}")

def b(l,b1,m):
    #print(l)
    print(f"a={m},b1= {b1}")
    return ((m)*l+b1)


l=np.linspace(l1,l2,10)
q=b(l,gg,m)
print("the answer is ",q)

e=np.linspace(0,0.3,10)
def t(l):
    print(-0.006666666666666666*l+ 0.0003)
t(e)