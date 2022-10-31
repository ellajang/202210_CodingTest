import sys

C = int(sys.stdin.readline())

for i in range(C):
    N_list=list(map(int,sys.stdin.readline().split()))
    avg = sum(N_list[1:])/N_list[0]
    cnt=0
    for i in N_list[1:]:
        if i > avg :
            cnt +=1
    total = cnt/N_list[0]*100
    print('{:.3f}%'.format(round(total,3)))       