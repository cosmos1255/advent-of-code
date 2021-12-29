# Day 6 Solution
# Problem found at https://www.adventofcode.com/2021/day/6

def parseInput(input):
    input = input[0].split(',')
    for i in range(len(input)):
        input[i] = int(input[i])
    return input

def add_buckets(buckets):
    sum = 0
    for num in buckets:
        sum += num
    return sum

def partone_two(latternfish, days):
    buckets = [0] * 9
    for fish in latternfish:
        buckets[fish] += 1
    for i in range(days):
        zeroth_bucket = buckets[0]
        for i in range(len(buckets)-1):
            buckets[i] = buckets[i+1]
        buckets[8] = zeroth_bucket
        buckets[6] += zeroth_bucket
    return add_buckets(buckets)

def daysix(input):
    input = parseInput(input)
    # print(input)
    print("Day 6 Solution:")
    # Comment partone to complete parttwo and vice versa
    print("PART1: Num of latternfish after 80 days: ", partone_two(input, 80))
    print("PART2: Num of latternfish after 256 days: ", partone_two(input, 256))