
X=int(input())

line=1
while X>line:
    X-=line
    line+=1
        
if line%2 == 0:
    a = X
    b = (line+1)-X
else:
    a = (line+1)-X
    b = X
    
print(a,'/',b,sep='')


""" 1. sep(separation) 
 

영단어 그대로, 분리하여 출력한다. 다만 분리할 (갈라놓을 문자를 지정할 수 있다.) 이것을 구분자라고 한다.

예를 들어서 아래처럼 사용 할 수 있다. """
    