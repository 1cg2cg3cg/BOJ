#import matplotlib.pyplot as plt
import math

#iter = int(input())
iter = 3

for k in range(iter) :
    print(k)

    x1, y1, r1, x2, y2, r2 = input().split()
    x1 = int(x1)
    y1 = int(y1)
    r1 = int(r1)
    x2 = int(x2)
    y2 = int(y2)
    r2 = int(r2)

    L = 0
    R = 0
    D = 0
    T = 0

    A = []
    B = []

    if (x1-r1) < (x2-r2) :
        L = (x1-r1)
    else :
        L = (x2-r2)

    if (x1+r1) < (x2+r2) :
        R = (x2+r2)
    else :
        R = (x1+r1)

    if (y1-r1) < (y2-r2) :
        D = (y1-r1)
    else :
        D = (y2-r2)

    if (y1+r1) < (y2+r2) :
        T = (y2+r2)
    else :
        T = (y1+r1)

    for a in range(L, R) :
        for b in range(D, T) :
            if ((a-x1)**2 + (b-y1)**2)**0.5 == r1 :
                A.append(a)
                B.append(b)

    c = 0
    for (i,j) in zip(A,B) :

        if (x2-i)**2 + (y2-j)**2 == r2**2 :
            c += 1

#plt.scatter(A,B)
#plt.show()

    if c == math.nan :
        print(-1)
    else :
        print(c)
