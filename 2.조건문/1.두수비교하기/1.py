#1.두 수 비교하기

import sys
A,B = sys.stdin.readline().split()

x=int(A)
y=int(B)

if x > y:
    print(">")
elif x < y:
    print("<")
else:
    print("==")    