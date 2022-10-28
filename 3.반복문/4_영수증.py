import sys
X=int(sys.stdin.readline())
N=int(sys.stdin.readline())
sum=0

for i in range(N):
   a,b=map(int,sys.stdin.readline().split())
   sum=sum + a*b

if sum == X:
    print("Yes")
else:
    print("No")