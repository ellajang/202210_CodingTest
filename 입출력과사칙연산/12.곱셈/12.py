# 12.곱셈

import sys

x=int(sys.stdin.readline())
y=int(sys.stdin.readline())

print(x*(y%10))
print(x*((y%100)//10))
print(x*(y//100))
print(x*y)

#split()는 같은 줄에 문자열을 구분하여 여러 입력을 받는 방법이다. 