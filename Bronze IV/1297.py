import math
a, b, c = map(int, input().split())
x = math.sqrt(a*a/((b*b)+(c*c))*b*b)
x = math.trunc(x)
y = math.sqrt(a*a/((b*b)+(c*c))*c*c)
y = math.trunc(y)
print(x,y)
