import sys
IN = sys.stdin.readline().split()
A = int(IN[0])
B = int(IN[1])
C = int(IN[2])
i = 0

if B >= C :
    print(-1)
else :
    print( A // (C-B) + 1)
