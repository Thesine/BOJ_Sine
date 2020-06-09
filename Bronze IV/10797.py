day = int(input())
l = list(map(int, input().split()))
num = 0
for i in range(len(l)):
  if day==l[i]:
    num = num+1
  else:
    pass
print(num)
