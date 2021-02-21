import sys

N = int(sys.stdin.readline().strip())

A = sys.stdin.readline().split()

Max = 0
result = 0

for i in range(N) :
    if int(A[i]) > Max :
        Max = int(A[i])

for i in range(N) :
    result += int(A[i])

result = result / (Max*N) * (100*N)

print(result/N)
