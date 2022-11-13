import sys

alphabet = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']


number = list(sys.stdin.readline())

time = 0
for i in number:
    for j in alphabet:
        if i in j:
            time += alphabet.index(j)+3

print(time)            
            
# index : list중 몇번째에 있는 지