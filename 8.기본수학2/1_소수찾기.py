import sys

N = int(sys.stdin.readline())
sosu = list(map(int,sys.stdin.readline().split()))
cnt = 0 

for i in sosu:
    if i > 1:
        for j in range(2,i) :
            if i % j == 0:
                break
    else:
        cnt += 1
print(cnt)