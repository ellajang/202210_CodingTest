# 계수 정렬 식

import sys

N = int(sys.stdin.readline())

li = [0]*10001 # 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)

for i in range(N):
    li[int(sys.stdin.readline())] += 1  # 각 데이터에 해당하는 인덱스의 값 증가

for i in range(len(li)):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)
            
# 결과를 확인할 때는 리스트의 첫 번째 데이터부터 하나씩 그 값만큼 반복하여 인덱스를 출력한다


