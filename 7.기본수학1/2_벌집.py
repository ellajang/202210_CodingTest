import sys

N = int(sys.stdin.readline())
mok = 1  
cnt = 1

while N > mok:
    mok += 6*cnt
    cnt += 1

print(cnt)

# mok += 6*cnt+1을 했을때 20과 같은 수를 넣었을 때, 3으로 출력된다. 