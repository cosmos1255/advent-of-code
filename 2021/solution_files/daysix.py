# Day 6 Solution
# Problem found at https://www.adventofcode.com/2021/day/6

def parseInput(input):
    input = input[0].split(',')
    for i in range(len(input)):
        input[i] = int(input[i])
    return input

def daysix(input):
    input = parseInput(input)
    # print(input)
    print("Day 6 Solution:")