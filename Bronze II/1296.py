oms = input()
n = int(input())
combi = 0
name = input()
for i in range(n-1):
  ss = input()
  L = oms.count('L')+ss.count('L')
  O = oms.count('O')+ss.count('O')
  V = oms.count('V')+ss.count('V')
  E = oms.count('E')+ss.count('E')
  score = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E))%100
  if score==combi:
    name = min(name,ss)
  elif score>combi:
    name = ss
    combi = score
  else:
    pass

print(name)
