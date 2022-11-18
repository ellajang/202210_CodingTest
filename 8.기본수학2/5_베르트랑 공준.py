import sys,math

def cool(n):
    if n==1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
           if n%i==0:
               return False
        return True

while True:
    N = int(sys.stdin.readline())
    if N == 0:
        break
    cnt = 0
    for i in range(N+1,2*N+1):
        if cool(i):
            cnt += 1
    print(cnt)        