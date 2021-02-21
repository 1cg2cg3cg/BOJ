iter = int(input())
XY = []

for k in range(iter) :
    X = input()
    XY.append(X)

for k in range(iter) :

    x1, y1, r1, x2, y2, r2 = XY[k].split()

    x1 = int(x1)
    y1 = int(y1)
    r1 = int(r1)
    x2 = int(x2)
    y2 = int(y2)
    r2 = int(r2)

    d = (x1-x2)**2 + (y1-y2)**2
    ra = (r1+r2)**2
    rb = (r1-r2)**2

    if x1==x2 and y1==y2 :
        if r1 == r2 :
            print(-1)
        else :
            print(0)
    else:
        if ra < d :
            print(0)
        elif ra == d :
            print(1)
        else :
            if rb == d :
                print(1)
            elif rb > d :
                print(0)
            else :
                print(2)
