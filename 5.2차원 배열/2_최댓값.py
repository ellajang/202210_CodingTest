import sys

board=[]

for i in range(9):
    board.append(list(map(int,sys.stdin.readline().split())))

x=0
y=0
Max=0

for i in range(9):
    for j in range(9):
        if board[i][j]>Max:
            Max=board[i][j]
            x=i+1
            y=j+1

print(Max)
print(x,y)