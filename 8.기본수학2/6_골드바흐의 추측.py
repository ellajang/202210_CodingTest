import sys,math

T = int(sys.stdin.readline())

def cool(n):
    if n == 1:
        return False
    else :
        for i in range(2, int(math.sqrt(n))+1):
            if n%i==0:
                return False
        return True

for i in range(T):
    N = int(sys.stdin.readline())
    a = int(N//2)
    b = int(N//2)
    while a > 0:
        if cool(a)==True and cool(b)==True:
            print(a,b)
            break
        else:
            a-=1
            b+=1    