a, b, c = map(int, input().split())
d = 0

if min(a,b,c) < a < max(a,b,c):
  d = a
elif min(a,b,c) < b < max(a,b,c):
  d = b
else:
  d = c

print(min(a,b,c), d, max(a,b,c))
