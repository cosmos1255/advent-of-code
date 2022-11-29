# Day 5 Solution
# Problem found at https://www.adventofcode.com/2021/day/5

def parseInput(input):
    coord_1_x = []
    coord_1_y = []
    coord_2_x = []
    coord_2_y = []
    for coord in input:
        coords = coord.split(' -> ')
        coords_1 = coords[0].split(',')
        coords_2 = coords[1].split(',')
        coord_1_x.append(int(coords_1[0], 10))
        coord_1_y.append(int(coords_1[1], 10))
        coord_2_x.append(int(coords_2[0], 10))
        coord_2_y.append(int(coords_2[1], 10))
    return (coord_1_x, coord_1_y, coord_2_x, coord_2_y)

def mark_danger(ocean, hor_vert, hor_vert_coord, p1, p2):
    if (p2 < p1):
        temp = p2
        p2 = p1
        p1 = temp
    if (hor_vert): # for vertical danger
        for i in range(p1, p2+1):
            ocean[i][hor_vert_coord] += 1
    if (not hor_vert): # for horizontal danger
        for i in range(p1, p2+1):
            ocean[hor_vert_coord][i] += 1

    return ocean

def count_danger_spaces(ocean, n):
    count = 0
    for i in range(n):
        for j in range(n):
            if (ocean[i][j] > 1):
                count += 1
    return count

def partone(c1x, c1y, c2x, c2y):
    ocean = [[0] * 1000] * 1000
    input_len = len(c1x)
    
    for i in range(input_len):
        if (c1x[i] == c2x[i]):
            ocean = mark_danger(ocean, 0, c1x[i], c1y[i], c2y[i])
        if (c1y[i] == c2y[i]):
            ocean = mark_danger(ocean, 1, c1y[i], c1x[i], c2x[i])
    # print(ocean)
    return count_danger_spaces(ocean, 1000)


def dayfive(input):
    (c1x, c1y, c2x, c2y) = parseInput(input)
    # print("c1 x and y: ", c1x, c1y)
    # print("c2 x and y: ", c2x, c2y)
    print("Day 5 Solution:")
    print("PART1: The number of unsafe spaces is: ", partone(c1x, c1y, c2x, c2y))