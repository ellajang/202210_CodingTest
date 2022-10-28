import sys

T=int(sys.stdin.readline())
A=T
count=0

while True:
    a=A//10
    b=A%10
    c=(a+b)%10
    A=(b*10)+c
    count += 1
    if A==T :
        break
    
print(count)


