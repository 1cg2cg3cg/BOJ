import sys

A = sys.stdin.readline().strip()

A = A.upper()
ABC = []
num = []

for i in range(len(A)) :
    if A[i] not in ABC :
        ABC.append(A[i])
        num.append(1)
    elif A[i] in ABC :
        num[ABC.index(A[i])] += 1

if num.count(max(num)) == 1 :
    print(ABC[num.index(max(num))])
else :
    print("?")
