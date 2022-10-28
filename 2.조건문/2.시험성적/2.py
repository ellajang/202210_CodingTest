#2.시험성적

import sys
x = int(sys.stdin.readline())

if 100>=x>=90:
    print("A")
elif 89>=x>=80:
    print("B")
elif 79>=x>=70:
    print("C")
elif 69>=x>=60:
    print("D")
else:
    print("F")