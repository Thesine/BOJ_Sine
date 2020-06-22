s = input()
sol = 0
for i in s:
  if i =='A' or i=='B' or i=='C':
    sol += 3
  elif i =='D' or i=='E' or i=='F':
    sol += 4
  elif i=='G' or i=='H' or i=='I':
    sol += 5
  elif i=='J' or i=='K' or i=='L':
    sol += 6
  elif i=='M' or i=='N' or i=='O':
    sol += 7
  elif i=='P' or i=='Q' or i=='R' or i=='S':
    sol += 8
  elif i=='T' or i=='U' or i=='V':
    sol += 9
  elif i=='W' or i=='X' or i=='Y' or i=='Z':
    sol += 10
print(sol) 
