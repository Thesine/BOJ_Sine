s = []

sum = 0
for j in range(8):
  s = input()
  
  for i in range(4):
    if (j+2)%2==0:
      if s[i*2]=='F':
        sum += 1
      else:
        pass
    else:
      if s[i*2+1]=='F':
        sum += 1
      else:
        pass  
print(sum)
