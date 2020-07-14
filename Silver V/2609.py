a,b = map(int, input().split())

lcm = a*b
gcd = 0
while True:
  gcd = max(a,b)%min(a,b)
  a, b = min(a,b), gcd
  if b == 0:
    gcd = a
    break

lcm //= gcd
print(gcd)
print(lcm)
