import sys
N = int(input())
li = []
for i in range(N):
  li.append(int(sys.stdin.readline()))
li.sort()
[print(i) for i in li]
