from calendar import c
from itertools import count
from re import S
import sys

T=[]

for t in range(10):
    A=int(sys.stdin.readline())
    B=A%42
    T.append(B)
    
s=set(T)
print(len(s))

# 중복되지 않고 순서가 없다라는 특징을 가진 set이다. set함수를 통해 중복된 값을 제거하여 나열해줄 수 있다. 
#  요소의 개수를 셀 때는 len 함수를 사용하면 된다.
# count함수는 문자열 내부에 특정 문자, 문자열이 포함되어 있는지 세어주는 함수이다. 