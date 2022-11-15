import sys

M = int(sys.stdin.readline()) # 작은 수
N = int(sys.stdin.readline()) # 큰 수 
MN = []

for i in range(M,N+1):
    if i > 1:
        for j in range(2,i): # i+1을 안하는 이유는 i가 포함되지 않은 가운데에 나눠지는 수가 있는지 찾기 위함이다 i가 포함되면 소수도 포함되는 것!
            if i % j == 0 :
                break
        else :
            MN.append(i)
            
if len(MN) == 0 :
    print(-1)
else :      
    print(sum(MN))  
    print(min(MN))  