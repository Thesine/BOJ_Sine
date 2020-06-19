n = int(input())
for j in range(n):
  s = input()
  acm = 0
  sum = 0
  for i in range(len(s)):
    if s[i]=='O':
      acm += 1
      sum = sum+acm
    else:
      acm = 0
  print(sum)
