# Day 2 Problem Solution
# Link to problem: https://adventofcode.com/2021/day/2

from typing import final


def parseInput(bin_str):
    bin_nums = []
    for ch in bin_str:
        bin_nums.append(int(ch, 10))
    # print(bin_nums)
    return bin_nums

def binToInt(bin_arr):
    arr_len = len(bin_arr)
    i = arr_len-1
    exp = 0
    num = 0
    while i >= 0:
        if (bin_arr[i] == 1):
            num += (2 ** exp)
            exp += 1
            i -= 1
        else:
            exp += 1
            i -= 1
    return num

def partone(input):
    final_bin_str = [0] * len(input[0])
    count = 0
    for str in input:
        bin_num_arr = parseInput(str)
        count += 1
        for (i, val) in enumerate(bin_num_arr):
            if val == 1:
                final_bin_str[i] += val
    gamma = []
    epsilon = []
    for i in final_bin_str:
        if (i >= count/2):
            gamma.append(1)
            epsilon.append(0)
        else:
            gamma.append(0)
            epsilon.append(1)
    # print(gamma)
    # print(epsilon)
    gamma_int = binToInt(gamma)
    epsilon_int = binToInt(epsilon)
    return (gamma_int, epsilon_int)

def parttwo(input):
    input_copy = input
    max_index = len(input_copy[0])
    for index in range(0, max_index):
        occurrence = 0
        count = 0
        for str in input_copy:
            val = int(str[index])
            count += 1
            if (val == 1):
                occurrence += 1
        if (occurrence >= count/2):
            occurrence = 1
        else:
            occurrence = 0
        for str in input_copy:
            if (occurrence != int(str[index])):
                input_copy.remove(str)
    o2 = parseInput(input_copy[0])
    co2 = []
    for i in o2:
        co2.append(int(not i))
    # print(input_copy)
    # print(o2)
    # print(co2)
    o2 = binToInt(o2)
    co2 = binToInt(co2)

    return (o2, co2)
 
def daythree(input):
    print("Day 3 Solution:")
    (gamma_1, epsilon_1) = partone(input)
    print("PART1: Gamma: {}, Epsilon: {}, Power consumption: {}".format(gamma_1, epsilon_1, gamma_1*epsilon_1)) # (2635, 1460, 3847100)
    (o2_rating, co2_scrubber) = parttwo(input)
    print("PART2: O2 Rating: {}, CO2 Scrubber: {}, Life Support rating: {}".format(o2_rating, co2_scrubber, o2_rating*co2_scrubber))