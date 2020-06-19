import sys
T = int(input())
for i in range(T):
  a, b = map(int, sys.stdin.readline().rstrip().split())
  print(a+b)
  
#sys.stdin.readline().split().rstrip()이 아니라 rstrip().split()이다
