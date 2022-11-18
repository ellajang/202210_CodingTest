import sys
import math

M,N=map(int, sys.stdin.readline().split())



for i in range(M,N+1):
    if i > 1:
        for j in range(2,int(math.sqrt(i)) + 1):
            if i % j == 0:
                break
        else :
            print(i)
            
            
""" 
소수를 판별하는 알고리즘이다.

소수들을 대량으로 빠르고 정확하게 구하는 방법이다.

단일 숫자 소수 여부 확인
어떤 수의 소수의 여부를 확인 할 때는, 특정한 숫자의 제곱근 까지만 약수의 여부를 검증하면 O(N^1/2)의 시간 복잡도로 빠르게 구할 수 있다.

수가 수(N이라고 가정)를 나누면 몫이 생기는데, 몫과 나누는 수 둘 중 하나는 N 제곱근 이하이기 때문이다.

만약, 대량의 소수를 한꺼번에 판별해야할 경우는 '에라토스테네스의 체'를 이용한다 """