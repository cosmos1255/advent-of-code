# Day 8 Solution
# Problem found at https://www.adventofcode.com/2021/day/8

def parseInput(input):
    input_strings = []
    for line in input:
        new_line = line.split(' ')
        new_line.remove('|')
        input_strings.append(new_line)
    return input_strings

def partone(input):
    # 1 = len 2
    # 4 = len 4
    # 7 = len 3
    # 8 = len 8
    count = 0
    for arr in input:
        n = len(arr)
        for i in range(10, n):
            str_len = len(arr[i])
            if (str_len == 2 or str_len == 4 or str_len == 3 or str_len == 7):
                count += 1
        # print(count, ": ", arr[10:14])
    return count

def dayeight(input):
    # 0-9 is first 10; 10-13 is output
    input = parseInput(input)
    # print(input)
    print("Day 8 Solution:")
    print("PART1: Number of 1, 4, 7, and 8 values: ", partone(input))