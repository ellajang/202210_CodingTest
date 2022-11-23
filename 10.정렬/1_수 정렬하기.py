import sys

N = int(sys.stdin.readline())
x = []

for i in range(N) :
    x.append(int(sys.stdin.readline()))

x.sort()

for i in x :
    print(i)