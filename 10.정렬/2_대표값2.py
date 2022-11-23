import sys

li = []

for i in range(0,5):
    li.append(int(sys.stdin.readline()))

li.sort()

print(int(sum(li)/5))
print(li[2])
