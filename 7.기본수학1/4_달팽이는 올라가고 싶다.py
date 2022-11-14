import sys

A,B,V = map(int,(sys.stdin.readline().split()))
#d가 day라고 했을 A가 올라가는 횟수는 d번 B가 내려가는 횟수는 d-1따라서 걸린시간인 V = Ad - B(d-1)  

d=(V-B)/(A-B)

if d == int(d):
    print(int(d))
else :
    print(int(d)+1)


