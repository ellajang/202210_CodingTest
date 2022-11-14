import sys

T = int(sys.stdin.readline())

for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    people = [i for i in range(1,n+1)]
    #리스트 = [ i for i in range(1, n+1) ]
    #새로운 리스트에 for반복문을 통해서 수를 1 ~ n 까지를 넣을 수 있다. => people = [] // for i in range(n,n+1) // people = [i]를 축약한 식이다. 
    for x in range(k):
        new = []
        for y in range(1,n+1):
            new.append(sum(people[:y]))
        people = new.copy()
    print(people[-1])
        
