import sys
from collections import Counter

N = int(sys.stdin.readline())
li = []

for i in range(N):
    li.append(int(sys.stdin.readline()))

# 평균값
sumN = round(sum(li)/N)
print(sumN)

# 중앙값
li.sort()
midN= li[(N//2)]
print(midN)

# 최대빈도수
count = Counter(li) #각 수에 대한 빈도수를 나타내주는 함수 //Counter({-2: 2, -1: 2, -3: 1})
cnt = count.most_common() # 빈도수를 수로 정리해주는 함수 [(-2, 2), (-1, 2), (-3, 1)]  -> [1][1] ==  (-1,2)에서 2번째인 2를 나타낸다. 

if len(cnt)>1: # len이 필요한 경우는 입력되는 값이 하나일 경우 에러발생 방지하기 위함이다. 
    if cnt[0][1]==cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

# 최댓값과 최솟값의 차이
print(max(li)-min(li))
    