# Advent of Code 2021!
# This is the main file for this project.
# 
# Link to AoC 2021: https://adventofcode.com/2021/

from solution_files.dayone import dayone
from solution_files.daytwo import daytwo
from solution_files.daythree import daythree

def fileIO_strings(filename):
    input_data = []
    with open(filename, "r") as file:
        input_data = [line for line in file.read().split('\n')]
    return input_data

def main():
    input_filename = './input-files/'
    # Day One solution
    d1_filename = input_filename + 'day-one-input.txt'
    d1_input = fileIO_strings(d1_filename)
    # print(d1_input)
    dayone(d1_input)

    # Day Two Solution
    d2_filename = input_filename + 'day-two-input.txt'
    d2_input = fileIO_strings(d2_filename)
    # print(d2_input)
    daytwo(d2_input)

    # Day Three Solution
    d3_filename = input_filename + 'day-three-input.txt'
    d3_input = fileIO_strings(d3_filename)
    # print(d3_input)
    daythree(d3_input)

if __name__=="__main__":
    main()
