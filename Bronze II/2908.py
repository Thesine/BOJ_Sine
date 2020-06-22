a, b = input().split()

sol_a = ''
sol_b = ''

for i in range(3):
  sol_a = sol_a + a[2-i]
  sol_b = sol_b + b[2-i]

print(max(sol_a,sol_b))
