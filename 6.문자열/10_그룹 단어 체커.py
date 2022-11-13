import sys
n = int(sys.stdin.readline())
cnt = n 
for i in range(n):
    word = sys.stdin.readline()
    for j in range(len(word)-1) :
        if word[j]== word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            #word j+1부터 끝까지 찾는다는 의미이다. 
            cnt -= 1
            break
print(cnt)