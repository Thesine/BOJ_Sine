N = int(input())
l = []
for i in range(N):
  l.append(int(input()))

if l[0]+l[2]==l[1]+l[1]:
  print(l[N-1]+l[1]-l[0])
elif l[0]*l[2]==l[1]*l[1]:
  print(l[N-1]*int(l[1]/l[0]))
  
#결과값 int로 나오게 나누는 부분 
