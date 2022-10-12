#3.윤년
from ast import And, Or
import sys
x = int(sys.stdin.readline())

if x%4==0 and (x%100!=0 or x%400==0*x):
    print("1")
else:print("0")
