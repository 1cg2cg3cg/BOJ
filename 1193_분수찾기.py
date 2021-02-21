import sys

N = int(sys.stdin.readline().strip())
i = 0

while N > 0 :
    i += 1
    N -= i

if i % 2 :
    print('{}/{}'.format(1-N, i+N))

else :
    print('{}/{}'.format(i+N, 1-N))
