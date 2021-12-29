# Day 7 Solution
# Problem found at https://www.adventofcode.com/2021/day/7

def parseInput(input):
    input = input[0].split(',')
    for i in range(len(input)):
        input[i] = int(input[i])
    return input

def dayseven(input):
    input = parseInput(input)
    print(input)