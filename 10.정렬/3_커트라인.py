import sys

N,k = map(int,sys.stdin.readline().split())

x = list(map(int,sys.stdin.readline().split()))

x.sort(reverse=True)
# x.sort()만 할 경우 오름차순으로 나열된다. 괄호 안 reverse=True를 입력하면 내림차순으로 입력된다. 

print(x[k-1])


