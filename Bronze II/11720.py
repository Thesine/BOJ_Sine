n = int(input())
s = ''
for i in range(n):
  s += input()
  if len(s)==n:
    break
sum = 0
for i in range(n):
  sum += int(s[i])

print(sum)
