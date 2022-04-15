from mpmath.libmp.libmpf import round_int
from mpmath import *
mp.dps = 25; 
a = sin(pi*34/180)**2 + sin(pi*56/180)**2 + 2*tan(pi*18/180)*tan(pi*72/180)
b =    cot(pi/6)**2
print(round(a-b,1))
