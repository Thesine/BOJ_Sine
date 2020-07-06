N = int(input())
li = list(map(int, input().split()))
li.sort()
print(li[0],li[N-1])
