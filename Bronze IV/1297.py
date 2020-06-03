import math
a, b, c = map(int, input().split())
x = math.sqrt(a*a//((b*b)+(c*c))*b*b)
x = math.floor(x)
y = math.sqrt(a*a//((b*b)+(c*c))*c*c)
y = math.floor(y)
print(x,y)
