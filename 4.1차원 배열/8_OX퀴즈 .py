import sys

T=int(sys.stdin.readline())

for i in range(T):
    T_list=list(sys.stdin.readline())
    result = 0
    sum_result = 0  
    for ox in T_list:
        if  ox == "O":
            result += 1
            sum_result += result
        else:
            result=0    
    print(sum_result)