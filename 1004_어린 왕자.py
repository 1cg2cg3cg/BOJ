iter = int(input())

for i in range(iter) :

    point = input().split()
    start = [int(point[0]),int(point[1])]
    goal = [int(point[2]),int(point[3])]
    c = 0

    planet = []

    num_planet = int(input())

    for i in range(num_planet) :
        X = input()
        planet.append(X)

    for i in range(num_planet) :
        planet_x, planet_y, planet_radius = planet[i].split()
        planet_x = int(planet_x)
        planet_y = int(planet_y)
        planet_radius = int(planet_radius)


        d1 = ((start[0] - planet_x)**2 + (start[1] - planet_y)**2)**0.5
        d2 = ((goal[0] - planet_x)**2 + (goal[1] - planet_y)**2)**0.5

        if planet_radius > d1 :
            if planet_radius > d2 :
                c += 0
            else :
                c += 1
        elif planet_radius > d2 :
            if planet_radius > d1 :
                c += 0
            else :
                c += 1

    print(c)
