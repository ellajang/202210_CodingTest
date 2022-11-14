import sys

T = int(sys.stdin.readline())


for i in range(T):
    H, W, N = map(int,sys.stdin.readline().split())
    Y = N % H
    XX = N // H + 1
    if  N % H == 0 :
        XX = N // H
        Y = H
    print(Y*100+XX)
    