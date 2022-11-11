import sys

N = int(sys.stdin.readline())
arr=[[0] * 101 for _ in range(101)]

for i in range(N):
    x,y=map(int,sys.stdin.readline().split())
    
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j]=1

result=0
for k in range(100):
    result += arr[k].count(1)        
# 1의 개수를 세는 것

print(result)

## 2차원 배열
## 1차원 list를 묶어놓은 list
## 세로 길이(행의 개수) = N, 가로 길이(열의 개수) = M 일때 2차원 배열 만들기
# arr = [[0] * M for _ in range(N)] 

# 아래와 같은 경우는 안됨!! 
# 모든 행이 같은 1차원 리스트를 참조하고 있기 때문 
#arr = [[0]*M]*N

