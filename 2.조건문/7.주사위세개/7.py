#7.주사위세개

import imp


import sys
A,B,C = map(int,sys.stdin.readline().split())

t = max(A,B,C)

if A==B==C :
    print(10000+A*1000)
elif A==B or A==C :
    print(1000+A*100)
elif B==C:
    print(1000+B*100)
elif A!=B!=C:
    print(t*100)
    