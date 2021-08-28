import sys
N, X=map(int,sys.stdin.readline().split())
A=map(int,sys.stdin.readline().split())

for small in A:
    if small<X:
        print(small, end=" ")
    else:
        continue