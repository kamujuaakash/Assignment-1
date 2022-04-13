from mpmath import mp
import math
mp.dps = 1
a = math.sin(math.pi*34/180)
b = math.sin(math.pi*56/180)
c = math.tan(math.pi*18/180)
d = math.tan(math.pi*72/180)
e = math.tan(math.pi*60/180)
result1 = mpf(a*a + b*b + 2*c*d )
result2 = mpf(e*e)
result = result1 - result2
print(result)
