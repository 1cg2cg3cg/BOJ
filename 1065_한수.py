import sys

N = int(sys.stdin.readline().strip())

number = 0

if N < 100 :
    number = N
    print(N)

else :
    number = 99

    for i in range(100, N+1) :
        A = str(i)
        Dif = []

        for j in range(1, len(A)) :
            Dif.append(int(A[j]) - int(A[j-1]))
        
        Dif = set(Dif)
        
        if len(Dif) == 1 :
            number += 1

    print(number)
