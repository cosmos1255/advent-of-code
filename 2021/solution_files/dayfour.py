# Day 4 Problem Solution
# Link to problem: https://adventofcode.com/2021/day/4

def check_boards_for_num(board, num):
    for i in range(0, 5):
        for j in range(0, 5):
            if (board[i][j] == num):
                board[i][j] = -1
    return board

def check_equal_nums(a, b, c, d, e):
    if (a == -1):
        if (a == b == c == d == e):
            return True
    return False

def check_winner(board):
    for i in range(0, 5):
        if (check_equal_nums(board[i][0], board[i][1], board[i][2], board[i][3], board[i][4])):
            return True
        if (check_equal_nums(board[0][i], board[1][i], board[2][i], board[3][i], board[4][i])):
            return True
    return False

def sum_unchecked(board):
    sum = 0
    for i in range(0, 5):
        for j in range(0, 5):
            if (board[i][j] != -1):
                sum += board[i][j]
    return sum

def boards_to_ints(input_boards):
    for board in input_boards:
        for i in range(0, 5):
            for j in range(0, 5):
                board[i][j] = int(board[i][j], 10)
    return input_boards

def partone(input, input_boards):
    for num in input:
        num = int(num)
        # print(num)
        for board in input_boards:
            board = check_boards_for_num(board, num)
            if (check_winner(board)):
                sum = 0
                sum = sum_unchecked(board)
                sum *= num # multiply by most recent number
                return sum 

def parttwo(input, input_boards):
    num_boards = len(input_boards)
    for num in input:
        num = int(num)
        # print(num)
        i = 0
        while i < num_boards:
            board = input_boards[i]
            board = check_boards_for_num(board, num)
            if (check_winner(board)):
                input_boards.remove(board)
                num_boards = len(input_boards)
                if (len(input_boards) == 0):
                    # print(i, ": ", board)
                    sum = 0
                    sum = sum_unchecked(board)
                    sum *= num
                    # print("final sum: ", sum, "; final num: ", num)
                    return sum
                continue
            i += 1

def dayfour(input, input_boards):
    input_boards = boards_to_ints(input_boards)
    sum = 0
    print("Day 4 solution:")
    # comment partone when running parttwo
    # sum = partone(input, input_boards)
    # print("PART1: The final score of part one is: ", sum) # 25023
    sum = parttwo(input, input_boards)
    print("PART2: The final score of part two is: ", sum) # 2634