import sys

N,M = map(int,sys.stdin.readline().split())

board=[]

for i in range(N):
    board.append(list(map(int,sys.stdin.readline().split())))

for i in range(N):
    A=list(map(int,sys.stdin.readline().split()))           

    for j in range(M):
        board[i][j] +=A[j] #2차원 배열 [1][2] -> 행열(1,2)

for i in range(N):
    for j in range(M):
        print(board[i][j],end=" ")
    print()
    