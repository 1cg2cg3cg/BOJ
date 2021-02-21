import sys

N = int(sys.stdin.readline().strip())
number = 0

for _ in range(N) :
    
    A = sys.stdin.readline().strip()
    stop = 0

    for i in range(len(A)) :
    
        start = A.index(A[i])
        end = A.rindex(A[i])

        if start != end :
            for j in range(start+1, end) :
                if A[start] != A[j] :
                    stop = 1
                    break

            if stop :
                break

    if not stop :
        number += 1

print(number)
