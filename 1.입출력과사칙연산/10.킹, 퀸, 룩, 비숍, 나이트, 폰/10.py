# 10.킹, 퀸, 룩, 비숍, 나이트, 폰
import sys

piece = [1,1,2,2,2,8]
inputPiece = list(map(int,sys.stdin.readline().split()))

for i in range(len(piece)):
    print(piece[i]-inputPiece[i],end=" ")



#len()은 리스트에 들어있는 원소 개수를 의미한다
# a = [1.2,3.4,5.44]
# map(int,input(a))
# a --> 정수 값으로  [1,3,5] 출력
# end를 공백으로 설정하면 같은 줄에 이어서 표시된다.