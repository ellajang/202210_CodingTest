import sys

T = [t for t in range(1,31)]

for t in range(28):
    n=int(sys.stdin.readline())
    T.remove(n)

print(T[0])
print(T[1])
