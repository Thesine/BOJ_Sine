A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
T = 0

if A<0:
  T = C*abs(A)+D+B*E
elif A==0:
  T = D+B*E
elif A>0:
  T = (B-A)*E

print(T)
