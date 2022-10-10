# 11.나머지
import sys
A,B,C=sys.stdin.readline().split()
x=int(A)
y=int(B)
z=int(C)

print((x+y)%z)
print(((x%z) + (y%z))%z)
print((x*y)%z)
print(((x%z)*(y%z))%z)