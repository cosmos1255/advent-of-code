# Day 10 Solution
# Problem found at https://www.adventofcode.com/2021/day/10

sym_table = [('[', ']'), ('{', '}'), ('(', ')'), ('<', '>')]

def check_open_sym(sym):
    if (sym == sym_table[0][0]):
        return True
    elif (sym == sym_table[1][0]):
        return True
    elif (sym == sym_table[2][0]):
        return True
    elif (sym == sym_table[3][0]):
        return True
    else:
        return False

def get_error_score(sym):
    if (sym == sym_table[0][1]):
        return 57
    elif (sym == sym_table[1][1]):
        return 1197
    elif (sym == sym_table[2][1]):
        return 3
    elif (sym == sym_table[3][1]):
        return 25137

def check_equal_syms(open_sym, close_sym):
    if (open_sym == sym_table[0][0] and close_sym == sym_table[0][1]):
        return True
    elif (open_sym == sym_table[1][0] and close_sym == sym_table[1][1]):
        return True
    elif (open_sym == sym_table[2][0] and close_sym == sym_table[2][1]):
        return True
    elif (open_sym == sym_table[3][0] and close_sym == sym_table[3][1]):
        return True
    else:
        return False

def partone(input):
    err_score = 0
    # line_cnt = 0
    for line in input:
        sym_stack = []
        # line_cnt += 1
        for sym in line:
            # print("Line ", line_cnt, ": ", sym_stack)
            if (check_open_sym(sym)):
                sym_stack.append(sym)
            else:
                last_sym = sym_stack[len(sym_stack)-1]
                if (check_equal_syms(last_sym, sym)):
                    sym_stack.pop()
                else:
                    err_score += get_error_score(sym)
                    break
    return err_score

def get_auto_comp_score(open_sym):
    if (open_sym == sym_table[0][0]):
        return 2
    elif (open_sym == sym_table[1][0]):
        return 3
    elif (open_sym == sym_table[2][0]):
        return 1
    elif (open_sym == sym_table[3][0]):
        return 4

def parttwo(input):
    auto_comp_scores = []
    for line in input:
        sym_stack = []
        line_score = 0
        for sym in line:
            # print("Line ", line_cnt, ": ", sym_stack)
            if (check_open_sym(sym)):
                sym_stack.append(sym)
            else:
                last_sym = sym_stack[len(sym_stack)-1]
                if (check_equal_syms(last_sym, sym)):
                    sym_stack.pop()
                else:
                    sym_stack = []
                    break
        while (sym_stack != []):
            last_sym = sym_stack[len(sym_stack)-1]
            line_score *= 5
            line_score += get_auto_comp_score(last_sym)
            sym_stack.pop()
        if (line_score != 0):
            auto_comp_scores.append(line_score)
    print(auto_comp_scores)
    auto_comp_scores.sort()
    print(len(auto_comp_scores))
    return auto_comp_scores[int(len(auto_comp_scores)/2)]

def dayten(input):
    # print(input)
    # print(sym_table)
    print("Day 10 Solution:")
    print("PART1: The total syntax error is:", partone(input))
    print("PART2: The total auto complete score is:", parttwo(input))