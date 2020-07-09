N, M = map(int, input().split())
li = list(map(int, input().split()))
a = len(li)
sol = 0
for i in range(0, a - 2):
  for j in range(i + 1, a - 1):
    for k in range(j + 1, a):
      if li[i] + li[j] + li[k] > M:
        continue
      else:
        sol = max(sol, li[i] + li[j] + li[k])
print(sol)
