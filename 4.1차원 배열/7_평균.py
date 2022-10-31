import sys

N = int(sys.stdin.readline())
N_list = list(map(int,sys.stdin.readline().split()))
T=max(N_list)

ls=[]
for i in N_list:
    ls.append(i/T*100)


result_ls=sum(ls)/N 
print(result_ls)   