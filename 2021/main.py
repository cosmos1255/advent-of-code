# Advent of Code 2021!
# This is the main file for this project.
# 
# Link to AoC 2021: https://adventofcode.com/2021/

from solution_files.dayone import dayone
from solution_files.daytwo import daytwo
from solution_files.daythree import daythree
from solution_files.dayfour import dayfour
from solution_files.dayfive import dayfive
from solution_files.daysix import daysix
from solution_files.dayseven import dayseven
from solution_files.dayeight import dayeight
from solution_files.daynine import daynine

def fileIO_bingo(filename):
    input_nums = []
    boards = []
    index = 0
    with open(filename, "r") as file:
        input_nums = file.readline().strip('\n').split(',') # first line with bingo nums
        while file.readline() != '':
            boards.append([])
            for i in range(0, 5):
                board_row = file.readline().strip('\n')
                board_row = board_row.split(' ')
                for item in board_row:
                    if (item == ''):
                        board_row.remove('')
                boards[index].append(board_row)
            index += 1
    return (input_nums, boards)

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
    print()

    # Day Two Solution
    d2_filename = input_filename + 'day-two-input.txt'
    d2_input = fileIO_strings(d2_filename)
    # print(d2_input)
    daytwo(d2_input)
    print()

    # Day Three Solution
    d3_filename = input_filename + 'day-three-input.txt'
    d3_input = fileIO_strings(d3_filename)
    # print(d3_input)
    daythree(d3_input)
    print()

    # Day Four Solution
    d4_filename = input_filename + 'day-four-input.txt'
    (d4_input, d4_input_boards) = fileIO_bingo(d4_filename)
    # print(d4_input)
    # print(d4_input_boards)
    dayfour(d4_input, d4_input_boards)
    print()

    # Day Five Solution
    d5_filename = input_filename + 'day-five-input.txt'
    d5_input = fileIO_strings(d5_filename)
    # print(d5_input)
    dayfive(d5_input)
    print()

    # Day Six Solution
    d6_filename = input_filename + 'day-six-input.txt'
    d6_input = fileIO_strings(d6_filename)
    # print(d6_input)
    daysix(d6_input)
    print()

    # Day Seven Solution
    d7_filename = input_filename + 'day-seven-input.txt'
    d7_input = fileIO_strings(d7_filename)
    # print(d7_input)
    dayseven(d7_input)
    print()

    # Day Eight Solution
    d8_filename = input_filename + 'day-eight-input.txt'
    d8_input = fileIO_strings(d8_filename)
    # print(d8_input)
    dayeight(d8_input)
    print()

    # Day Nine Solution
    d9_filename = input_filename + 'day-nine-input.txt'
    d9_input = fileIO_strings(d9_filename)
    print(d9_input)
    daynine(d9_input)
    print()

if __name__=="__main__":
    main()
