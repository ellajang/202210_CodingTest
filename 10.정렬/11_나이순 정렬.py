import sys

N = int(sys.stdin.readline())

li = []

for i in range(N):
    x,y=map(str,sys.stdin.readline().split())
    li.append((int(x),i,y))
    
li.sort()
    
for i in range(N):
    print(li[i][0],li[i][2])