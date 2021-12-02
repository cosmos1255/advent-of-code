# Day 2 Problem Solution
# Link to problem: https://adventofcode.com/2021/day/2

def parseInputStr(str):
    (command, value) = str.split(' ')
    # print("com:", command)
    # print("val:", value)
    return (command, value)

def part_one(input):
    x = 0
    y = 0
    for str in input:
        (command, value) = parseInputStr(str)
        value = int(value, 10)
        if command == 'forward':
            x += value
        elif command == 'up':
            y -= value
            if (y < 0 ):
                y = 0
        elif command == 'down':
            y += value
    # print(x, " ", y)
    return x*y

def part_two(input):
    x = 0
    y = 0
    aim = 0
    for str in input:
        (command, value) = parseInputStr(str)
        value = int(value, 10)
        if command == 'forward':
            x += value
            y += (value * aim)
        elif command == 'up':
            aim -= value
        elif command == 'down':
            aim += value
    # print(x, " ", y, " ", aim)
    return x*y

def daytwo(input):
    
    print("Day 2 Solution:")
    print("PART1: The final x and y position mulitplied is: ", part_one(input)) # 1947824
    print("PART2: The final x and y position multiplied with aim accounted is: ", part_two(input)) # 1813062561