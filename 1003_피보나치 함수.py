def FIBO(n) :
    if n == 0 :
        A.append([1,0])
    elif n == 1:
        A.append([0,1])
    else :
        X = [A[n-2][0] + A[n-1][0], A[n-2][1] + A[n-1][1]]
        A.append(X)


iter = int(input())
init = []

for i in range(iter) :
    X = input()
    init.append(X)


for j in range(iter) :
    A = []
    k = int(init[j])

    for i in range(k+1) :
        FIBO(i)

    print(A[-1][0], A[-1][1])
