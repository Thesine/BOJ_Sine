s = input()
pr = ''
cnt = 0
for i in s:
  cnt += 1
  pr = pr + i
  if cnt%10==0:
    print(pr)
    pr = ''
  else:
    pass
print(pr)
