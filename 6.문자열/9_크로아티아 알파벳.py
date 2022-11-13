import sys

croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

word = sys.stdin.readline().rstrip()
#rstrip([chars]) : 인자로 전달된 문자를 String의 오른쪽에서 제거합니다.-> 동일 문자 제거를 위함
for i in croatia :
    word = word.replace(i,'^')
print(len(word)) 



 
