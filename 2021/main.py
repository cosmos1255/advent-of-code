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
from solution_files.dayten import dayten
from solution_files.dayeleven import dayeleven

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
    day_filenames = ['day-one-input.txt', 'day-two-input.txt', 'day-three-input.txt', 
        'day-four-input.txt', 'day-five-input.txt', 'day-six-input.txt', 'day-seven-input.txt', 
        'day-eight-input.txt', 'day-nine-input.txt', 'day-ten-input.txt', 'day-eleven-input.txt']
    inputs = []

    for i, day in enumerate(day_filenames):
        filename = input_filename + day
        print(filename, ' ', i)
        if (i == 3): # day 4
            (input_0, input_1) = fileIO_bingo(filename)
            inputs.append(input_0)
            inputs.append(input_1)
            continue
        else: # day 1-3, 5-25
            input = fileIO_strings(filename)
            inputs.append(input)

    # print(inputs)
            
    # Day One solution
    dayone(inputs[0])
    print()

    # Day Two Solution
    daytwo(inputs[1])
    print()

    # Day Three Solution
    daythree(inputs[2])
    print()

    # Day Four Solution
    # dayfour(3: input, 4: input_boards)
    dayfour(inputs[3], inputs[4])
    print()

    # Day Five Solution
    dayfive(inputs[5])
    print()

    # Day Six Solution
    daysix(inputs[6])
    print()

    # Day Seven Solution
    dayseven(inputs[7])
    print()

    # Day Eight Solution
    dayeight(inputs[8])
    print()

    # Day Nine Solution
    daynine(inputs[9])
    print()

    # Day Ten Solution
    dayten(inputs[10])
    print()

    # Day Eleven Solution
    dayeleven(inputs[11])
    print()

if __name__=="__main__":
    main()
