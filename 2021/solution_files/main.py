# Advent of Code 2021!
# This is the main file for this project.
# 
# Link to AoC 2021: https://adventofcode.com/2021/

import dayone

def fileIO_strings(filename):
    input_data = []
    with open(filename, "r") as file:
        input_data = [line for line in file.read().split('\n')]
    return input_data

def main():
    # Day One solution
    d1_filename = '../input-files/day-one-input.txt'
    d1_input = fileIO_strings(d1_filename)
    # print(d1_input)
    dayone.solution(d1_input)

if __name__=="__main__":
    main()
