x, y = map(int, input().split())
Mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
Day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

for i in range(x-1):
  y += Mon[i]

print(Day[y%7])
