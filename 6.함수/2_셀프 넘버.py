def d(n):
    n=n+sum(map(int,str(n)))
    return n

solve_s=set()

for i in range(1,10001):
    solve_s.add(d(i))
    
for j in range(1,10001):
    if j not in solve_s:
        print(j)

    
    
    
# str 명령을 써서 숫자를 문자열 자료형으로 바꾸어야 한다
#set()을 통해서 자료형 리스트를 만들수 있다. -> 중복은 없고 순서도 없다.
# 예를들어
# s2 = set("hello")
# print(s2)
# result : {'o', 'h', 'l', 'e'}

