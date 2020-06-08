k, n, m = map(int, input().split())

if m>k*n:
  print("0")
else:
  print(abs(k*n-m))
