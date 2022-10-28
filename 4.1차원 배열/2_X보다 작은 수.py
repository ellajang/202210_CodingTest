import sys
N,X = map(int,sys.stdin.readline().split())
M_list=list(map(int,sys.stdin.readline().split()))

for i in range(N):
    if M_list[i] < X:
        print(M_list[i],end=" ")