"""Advent of Code 2023, Day: 1
Author: David Eyrich
Link: https://adventofcode.com/2023/day/1"""

from curses.ascii import isalnum, isalpha
import os
import sys

scripts_path = os.getcwd()
scripts_path_split = scripts_path.split('/')
scripts_path_join = '/'.join(scripts_path_split[:-2])
sys.path.append(f"{scripts_path_join}/aoc_mod/src")

from sess_id_u_agent import USER_AGENT, SESSION_ID
from submit_ans import submit

def parseInput(filename):
    # read in from a file
    with open(filename, 'r') as f:
        input = f.read()
    
    # parse through input here
    parsedInput = input.split('\n')
    
    return parsedInput

def partA(input):
    print("Part A")
    
    sum = 0
    
    # print(input)
    for line in input:
        a = 0
        b = 0
        for ch in line:
            if not isalpha(ch):
                a = ch
                break
        for ch in line[::-1]:
            if not isalpha(ch):
                b = ch
                break
        digit = int(a + '' + b)
        sum += digit
    
    return sum

def partB(input):
    print("Part B")
    
    let_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    sum = 0
    
    # print(input)
    for line in input:
        a = 0
        a_pos = 0
        b = 0
        b_pos = 0
        c = 0
        c_pos = 100000000
        d = 0
        d_pos = 0
        
        for i, let_num in enumerate(let_nums):
            tmp = line.find(let_num)
            if tmp != -1 and tmp < c_pos:
                c_pos = tmp
                c = i+1
                
            tmp = line.rfind(let_num)
            if tmp != -1 and tmp > d_pos:
                d_pos = tmp
                d = i+1
        
        # print(indices)
        for i, ch in enumerate(line):
            if not isalpha(ch):
                a = ch
                a_pos = i
                break
        for i, ch in enumerate(line[::-1]):
            if not isalpha(ch):
                b = ch
                b_pos = len(line)-1-i
                break
        
        if c_pos < a_pos:
            a = c
        if d_pos > b_pos:
            b = d
                        
        digit = int(f"{a}{b}")
        
        # print(digit, a_pos, b_pos, c_pos, d_pos)
        sum += digit
    
    return sum

def entry():
    print("2023:Day1")
    input = parseInput("day1_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2023, 1, SESSION_ID, USER_AGENT)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2023, 1, SESSION_ID, USER_AGENT)

if __name__=="__main__":
    entry()