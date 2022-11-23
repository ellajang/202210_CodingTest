import sys

N = int(sys.stdin.readline())

result = 0
multiple = 1

if N == 1 :
    result = (54/54)
elif N == 2:
    result = ((2/54)*(1/53)) + ((13/54)*(12/53))*4
elif N <= 13 :
    for i in range(N):   
        multiple = multiple*((13-i)/(54-i))
    result = multiple*4
else:
    result = 0

print(result)