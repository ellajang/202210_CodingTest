import sys

sugar = int(sys.stdin.readline())
bag =0

while sugar>0:
    if sugar % 5 == 0 :
        bag += int(sugar//5)
        print(bag)
        break
    sugar  = sugar - 3
    bag += 1
else:
    print(-1)
