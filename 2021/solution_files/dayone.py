# Day 1 Problem Solution
# Link to problem: https://adventofcode.com/2021/day/1

def part_one(input, input_len):
    count = 0
    for i in range(0, input_len-1):
        if (input[i] < input[i+1]):
            count+=1
    return count

def part_two(input, input_len):
    count = 0
    for i in range(0, input_len-3):
        (a, b, c, d) = input[i], input[i+1], input[i+2], input[i+3]
        first_trip = a + b + c
        second_trip = b + c + d
        if (first_trip < second_trip):
            count+=1
    return count

def dayone(input):
    # process input
    input_len = len(input)
    new_list = []
    for i in range(0, input_len):
        new_list.append(int(input[i], 10))

    print("Day 1 Solution:")                                            # Answers:
    print("PART1: The final count is: ", part_one(new_list, input_len)) # 1676
    print("PART2: The final count is: ", part_two(new_list, input_len)) # 1706
