import math
a, b = map(int, input().split())
na = a%4
nb = b%4

if na == 0:
  na = 4
elif nb == 0:
  nb = 4
else:
  pass

print(abs(na-nb) + math.ceil(max(a,b)/4)-math.ceil(min(a,b)/4))
