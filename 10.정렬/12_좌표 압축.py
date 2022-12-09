import sys

N = int(sys.stdin.readline())

x = list(map(int,sys.stdin.readline().split("")))

new_x = sorted(set(x))
