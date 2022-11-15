import sys

N = int(sys.stdin.readline())

for i in range(2,N+1):
    if N%i == 0:
        while N%i == 0:
            print(i)  
            N=N/i
        