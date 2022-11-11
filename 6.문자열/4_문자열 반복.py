T = int(input())
for i in range(T):
    num,S = input().split()
    for x in S:
        print(x*int(num),end='')        
    print()
    
    #for문 첫 줄의 기본구조는 [ for 변수 in iterable ]이다. 이후 수행할 문장은 한 칸 아래에 들여 쓰기 해서 작성한다. 이때 반복 가능한 iterable 자료형은 문자열도 포함이 된다. 문자열을 iterable 자리에 입력하면 문자열의 각 문자를 분리해서 변수에 선언한다.