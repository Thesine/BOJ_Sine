s = input()
sol = len(s)
li = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in li:
  if s.count(i)>0:
    sol -= s.count(i)

print(sol)
