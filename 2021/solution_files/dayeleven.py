# Day 11 Solution
# Problem found at https://www.adventofcode.com/2021/day/11

def parseInput(input):
    octopus_map = []
    for line in input:
        line_map = []
        for ch in line:
            line_map.append(int(ch))
        octopus_map.append(line_map)
    return octopus_map

def flash(octo_map, x, y, coord_queue):
    octo_map[x][y] = 0
    

def partone(octo_map):
    coord_queue = []
    input_len = len(octo_map)
    for i in range(input_len):
        for j in range(input_len):
            num = octo_map[i][j]
            if (num < 9 and num >= 0):
                octo_map[i][j] += 1
            elif (num == 9 or num == -1):
                octo_map[i][j] = -1
                flash(octo_map, i, j, coord_queue)


def dayeleven(input):
    octo_map = parseInput(input)
    print("Day 11 Solution:")
    print("PART1: Total flashes after 100 steps: ", partone(octo_map))