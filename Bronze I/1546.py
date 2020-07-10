N = int(input())
li = list(map(int, input().split()))
li.sort()
avg = li[-1]
sum = 0
for i in li:
  sum += i/avg*100
print(sum/N)
