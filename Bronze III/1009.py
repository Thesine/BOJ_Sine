T = int(input())
l = []
for i in range(T):
  a, b = map(int, input().split())
  a = a%10
  if a==1 or a==3 and b%4==0 or a==7 and b%4==0 or a==9 and b%2==0:
    l.append(1)
  elif a==2 and b%4==1 or a==8 and b%4==3:
    l.append(2)
  elif a==2 and b%4==2 or a==8 and b%4==2 or a==4 and b%2==1:
    l.append(4)
  elif a==2 and b%4==3 or a==8 and b%4==1:
    l.append(8)
  elif a==2 and b%4==0 or a==6 or a==8 and b%4==0 or a==4 and b%2==0:
    l.append(6)
  elif a==3 and b%4==1 or a==7 and b%4==3:
    l.append(3)
  elif a==3 and b%4==2 or a==7 and b%4==2 or a==9 and b%2==1:
    l.append(9)
  elif a==3 and b%4==3 or a==7 and b%4==1:
    l.append(7)
  elif a==5:
    l.append(5)
  elif a==0:
    l.append(10)

for j in range(len(l)):
  print(l[j])
