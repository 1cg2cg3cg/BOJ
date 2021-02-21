import random

def factorial(n) :
    if n == 0 :
        return 0
    elif n== 1:
        return 1
    else :
        return factorial(n-1) + factorial(n-2)

iter = int(input())

for i in range(iter) :
    N = int(input())

    xy = []
    for i in range(N) :
        a, b = input().split()
        xy.append([int(a),int(b)])

    S = []
    print(N)

    for i in range(factorial(N)) :
        X = xy[0][0]
        Y = xy[0][1]
        print("i ", i)
        print(xy)

        for n in range(1,N) :
            X += xy[n][0]
            Y += xy[n][1]
            print("n ", n)

        S.append((X**2 + Y**2)**0.5)
        random.shuffle(xy)

    print(S)
    print("result ", min(S))
