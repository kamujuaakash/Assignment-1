import math

a = math.sin(math.pi*34/180)
b = math.sin(math.pi*56/180)
c = math.tan(math.pi*18/180)
d = math.tan(math.pi*72/180)
e = math.tan(math.pi*60/180)
result = int(a*a + b*b + 2*c*d - e*e)
print(result)
