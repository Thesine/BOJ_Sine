x, y, w, h = map(int, input().split())
print(min(w-x,h-y,x,y))
#x,y도 고려해줘야 한다
