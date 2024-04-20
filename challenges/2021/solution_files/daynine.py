# Day 9 Solution
# Problem found at https://www.adventofcode.com/2021/day/9

def parseInput(input):
    new_input = []
    for line in input:
        line = [int(ch) for ch in line]
        # print(line)
        new_input.append(line)
    return new_input

def isRiskArea(num, le, bot, ri, top):
    dirs = [le, bot, ri, top]
    for dir in dirs:
        if (dir == -1):
            continue
        if (dir <= num):
            return False
    return True


def partone(input):
    line_len = len(input)
    num_lines = len(input[0])

    risk_level = 0
    # corner [0,0] (upper-left)
    num = input[0][0]
    ri = input[1][0]
    bot = input[0][1]
    if (ri > num and bot > num):
        risk_level += (num + 1)
    # corner [line_len-1, 0] (upper-right)
    num = input[line_len-1][0]
    le = input[line_len-2][0]
    bot = input[line_len-1][1]
    if (le > num and bot > num):
        risk_level += (num + 1)
    # corner [0, num_lines-1] (bottom-left)
    num = input[0][num_lines-1]
    ri = input[0][num_lines-2]    
    top = input[1][num_lines-1]
    if (ri > num and top > num):
        risk_level += (num + 1)
    # corner [line_len-1, num_lines-1] (bottom-right)
    num = input[line_len-1][num_lines-1]
    le = input[line_len-2][num_lines-1]
    top = input[line_len-1][num_lines-2]
    if (le > num and top > num):
        risk_level += (num + 1)
            
    for i in range(line_len):
        for j in range(num_lines):
            num = input[i][j]
            le = ri = bot = top = -1
            # check for 4 corners of input
            if ((i ==0 and j == 0) or (i == 0 and j == num_lines-1) or (i == line_len-1 and j == 0) or (i == line_len-1 and j == num_lines-1)):
                continue
            if (j == 0):
                le = input[i-1][j]
                bot = input[i][j+1]
                ri = input[i+1][j]
            elif (j == num_lines-1):
                le = input[i-1][j]
                top = input[i][j-1]
                ri = input[i+1][j]
            elif (i == 0):
                top = input[i][j-1]
                bot = input[i][j+1]
                ri = input[i+1][j]
            elif (i == line_len-1):
                top = input[i][j-1]
                bot = input[i][j+1]
                le = input[i-1][j]
            else:
                le = input[i-1][j]
                bot = input[i][j+1]
                ri = input[i+1][j]
                top = input[i][j-1]

            if (isRiskArea(num, le, bot, ri, top)):
                risk_level += (num+1)
    return risk_level

def findBasin(input, i, j):
    num = input[i][j]


def parttwo(input):
    line_len = len(input)
    num_lines = len(input[0])

    risk_level = 0
    # corner [0,0] (upper-left)
    num = input[0][0]
    ri = input[1][0]
    bot = input[0][1]
    if (ri > num and bot > num):
        risk_level += (num + 1)
    # corner [line_len-1, 0] (upper-right)
    num = input[line_len-1][0]
    le = input[line_len-2][0]
    bot = input[line_len-1][1]
    if (le > num and bot > num):
        risk_level += (num + 1)
    # corner [0, num_lines-1] (bottom-left)
    num = input[0][num_lines-1]
    ri = input[0][num_lines-2]    
    top = input[1][num_lines-1]
    if (ri > num and top > num):
        risk_level += (num + 1)
    # corner [line_len-1, num_lines-1] (bottom-right)
    num = input[line_len-1][num_lines-1]
    le = input[line_len-2][num_lines-1]
    top = input[line_len-1][num_lines-2]
    if (le > num and top > num):
        risk_level += (num + 1)
            
    for i in range(line_len):
        for j in range(num_lines):
            num = input[i][j]
            le = ri = bot = top = -1
            # check for 4 corners of input
            if ((i ==0 and j == 0) or (i == 0 and j == num_lines-1) or (i == line_len-1 and j == 0) or (i == line_len-1 and j == num_lines-1)):
                continue
            if (j == 0):
                le = input[i-1][j]
                bot = input[i][j+1]
                ri = input[i+1][j]
            elif (j == num_lines-1):
                le = input[i-1][j]
                top = input[i][j-1]
                ri = input[i+1][j]
            elif (i == 0):
                top = input[i][j-1]
                bot = input[i][j+1]
                ri = input[i+1][j]
            elif (i == line_len-1):
                top = input[i][j-1]
                bot = input[i][j+1]
                le = input[i-1][j]
            else:
                le = input[i-1][j]
                bot = input[i][j+1]
                ri = input[i+1][j]
                top = input[i][j-1]

            if (isRiskArea(num, le, bot, ri, top)):
                risk_level += (num+1)
    return risk_level
                
def daynine(input):
    input = parseInput(input)
    # print(input)
    print("Day 9 Solution:")
    print('PART1: The sum of risk levels is: ', partone(input))
    print('PART2: The product of the 3 largest basins is: ', parttwo(input))