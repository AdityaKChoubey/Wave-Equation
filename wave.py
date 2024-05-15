import matplotlib.pyplot as plt
import numpy as np

#parameters
L = 10
x0 = 5
k = 10
Tf = 25
v = 1
x,dx = np.linspace(0,L,1001,retstep = True)
t,dt = np.linspace(0,Tf,4001,retstep = True)

print(dx,dt)
r = (v*dt)/dx    #CFL condition
c = r**2

#gaussian pluck


def Io(x):
 u = np.exp(-k*(x-x0)**2)
 return u
 
def g(x):
 return 0.0
 
 
 
U = np.zeros((len(x),len(t)))

#boundary
U[0,:] = 0.0  #U at zero at all time 
U[-1,:] = 0.0  # U at other end at all time
U[:,0] = Io(x)


for XX in range(1,len(x)-1):
 U[XX,1] = 0.5*(c*U[XX+1,0] + 2*(1-c)*U[XX,0]+c*U[XX-1,0]) + dt*g(x)
for tt in range(1,len(t)-1):
 for XX in range(1,len(x)-1):
  U[XX,tt+1] = c*U[XX+1,tt] + 2*(1-c)*U[XX,tt]+c*U[XX-1,tt] - U[XX,tt-1]
  
  
  
for T in range(0,len(t),350):
 plt.plot(x,U[:,T],ls='-.',lw = 1 , label = 't='+str(T))
 
#plt.legend(loc = 'best')
plt.tight_layout()
plt.grid
plt.pause(10)

plt.show()
