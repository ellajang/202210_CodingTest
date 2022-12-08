import sys

N=int(sys.stdin.readline().rstrip())

li = set(sys.stdin.readline().rstrip()for _ in range(N)) 
""" -> sys.stdin.readline()를 반복  """
""" set은 중복값을 제거해준다 """
"""rstrip()는 공백을 없애준다."""
setli = list(li)
    
setli.sort()
'''sort는 알파벳 순으로 정렬해준다. '''
setli.sort(key=len)  
'''sort(key=len) 길이 순으로 정렬해준다. '''

for i in setli:
    print(i)    