# Day 7 Solution
# Problem found at https://www.adventofcode.com/2021/day/7

def parseInput(input):
    input = input[0].split(',')
    for i in range(len(input)):
        input[i] = int(input[i])
    return input

def isSorted(input):
    for i in range(1, len(input)):
        if (input[i-1] > input[i]):
            return False
    return True

def sortInput(input):
    for i in range(0, len(input)):
        min = 9999999999
        min_index = 0
        for j in range(i, len(input)):
            if (min > input[j]):
                min = input[j]
                min_index = j
        temp = input[i]
        input[i] = input[min_index]
        input[min_index] = temp
        # print(i, ": ", min_index)
    return input

def partone(input):
    input = sortInput(input)
    # print(input)
    avg = 0
    for num in input:
        avg += num
    avg = int(avg / len(input))
    median = input[int(len(input)/2)+1]

    p1 = 0
    p2 = 0
    if (avg < median):
        p1 = avg
        p2 = median
    else:
        p1 = median
        p2 = avg
    p1 -= 10
    p2 += 10
    min_moves = 999999999
    for pivot in range(p1, p2):
        moves = 0
        for num in input:
            moves += int(abs(pivot - num))
        if (moves < min_moves):
            min_moves = moves
    return min_moves

# function used to add numbers from n (n + n-1 + n-2 + ... + 1)
def addUp(num):
    sum = 0
    for i in range(1, num+1):
        sum += i
    return sum

def parttwo(input):
    # print(input)
    min_moves = 999999999
    p1 = 0
    p2 = len(input)-1
    for pivot in range(p1, p2):
        moves = 0
        for num in input:
            old_moves = int(abs(pivot - num))
            moves += addUp(old_moves)
        if (moves < min_moves):
            min_moves = moves
    return min_moves

def dayseven(input):
    input = parseInput(input)
    input = sortInput(input)
    # print(input)
    print("Day 7 Solution:")  
    print("PART1: Fuel used: ", partone(input))
    # print("PART2: Fuel used with new adding: ", parttwo(input))