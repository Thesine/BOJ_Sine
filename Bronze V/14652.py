m, n, k = map(int, input().split())

for i in range(1, m):
  for j in range(1, n):
    if(i*j==k):
      print(i-1,j-1)
