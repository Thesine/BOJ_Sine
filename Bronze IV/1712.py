import math
a, b, c = map(int, input().split())

if c==b or c<b:
  print("-1")
else:
  x = a//(c-b)+1
  print(math.ceil(x))
