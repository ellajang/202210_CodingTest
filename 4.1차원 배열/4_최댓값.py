
import sys
T = []

for i in range(9):
    T.append(int(sys.stdin.readline()))

print(max(T))
print(T.index(max(T))+1)