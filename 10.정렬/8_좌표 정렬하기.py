import sys

N=int(sys.stdin.readline())

li = []

for i in range(N):
    x,y=map(int,(sys.stdin.readline().split()))
    li.append((x,y))

li.sort()

for i in range(N):
    print(li[i][0],li[i][1])