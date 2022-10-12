# 6.오븐시계

import sys
A,B = map(int,sys.stdin.readline().split())
C = int(sys.stdin.readline())

A += (C//60)
B += (C%60)

if B>=60:
    A += 1
    B -= 60
if A>=24:
    A-=24
print(A,B)




"""
아래는 처음 작성한 방법 

if C>59 :
    if B+(C%60) > 59:
        if (A+(C//60)+1) > 23:
            print((A+(C//60)+1)-24,B+(C%60)-60)
        else:
            print(A+(C//60)+1,B+(C%60)-60)    
    else:
        if A+(C//60)>23:
            print(A+(C//60)-24,B+(C%60))
        else:
            print(A+(C//60),B+(C%60))
elif C<60:
    if B+C > 59:
        if A+1 >23:
            print((A+1)-24,B+C-60)
        else:
            print(A+1,B+C-60)
    else:
        if A>23:
            print(A-24,B+C)
        else: print(A,B+C) """
            
    
    
    
    