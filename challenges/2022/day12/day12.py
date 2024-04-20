"""Advent of Code 2022, Day: 12
Author: David Eyrich
Link: https://adventofcode.com/2022/day/12"""

import os
from collections import deque
import sys
import time

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

def printInputClone(input_clone):
    for line in input_clone:
        print(''.join(line))
    print()
    time.sleep(0.05)
    
def isValidMove(new, old, input):    
    if ord(input[new[0]][new[1]]) <= ord(input[old[0]][old[1]])+1:
        return 1
    return 0

def visit(n, input):
    i, j = n
    adj = []
    
    if i != len(input)-1: # grab down
        # print('down')
        if isValidMove((i+1,j), n, input):
            adj.append((i+1, j))
    if j != len(input[0])-1: # grab right
        # print('right')
        if isValidMove((i,j+1), n, input):
            adj.append((i, j+1))
    if i != 0: # grab up
        # print('up')
        if isValidMove((i-1,j), n, input):
            adj.append((i-1, j))
    if j != 0: # grab left
        # print('left')
        if isValidMove((i,j-1), n, input):
            adj.append((i, j-1))
        
    return adj
        

def search(start, end, input, input_clone):
    path_len = 0
    
    visited = set()

    q = deque()
    visited.add(start)

    # input_clone[start[0]][start[1]] = '*'
    q.append(start)
    
    while len(q) != 0:
        # print(path_len)
        # printInputClone(input_clone)
        size = len(q)

        while (size):
            n = q.popleft()
            if n == end:
                return path_len
            
            adj = visit(n, input)
            
            # print(adj)
            for a in adj:
                if a not in visited:
                    # input_clone[a[0]][a[1]] = '*'
                    visited.add(a)
                    q.append(a)
            size-=1
        path_len += 1
        
    return -1


def partA(input, input_clone):
    print("Part A")
    
    s_found = 0
    e_found = 0 
    start = 0
    end = 0
    
    for i, line in enumerate(input):
        input[i] = list(line)
        
    for i, line in enumerate(input_clone):
        input_clone[i] = list(line)
        
    # print(input)
    # print(input_clone)
    
    # locate S and E
    for i, line in enumerate(input):
        for j, ch in enumerate(line):
            if ch == 'S':
                start = (i,j)
                s_found = 1
            if ch == 'E':
                end = (i,j)
                e_found = 1
            if s_found and e_found:
                break        
                
    input[start[0]][start[1]] = 'a'
    input[end[0]][end[1]] = 'z'           
    
    return search(start, end, input, input_clone)

def partB(input, input_clone):
    print("Part B")
    
    starts = []
    old_start = 0
    end = 0
    
    for i, line in enumerate(input):
        input[i] = list(line)
        
    for i, line in enumerate(input_clone):
        input_clone[i] = list(line)
        
    # print(input)
    # print(input_clone)
    
    # locate S and E
    for i, line in enumerate(input):
        for j, ch in enumerate(line):
            if ch == 'a':
                starts.append((i,j))
            if ch == 'S':
                old_start = (i,j)
                starts.append((i,j))
            if ch == 'E':
                end = (i,j)     
                
    input[old_start[0]][old_start[1]] = 'a'
    input[end[0]][end[1]] = 'z'          
    
    lowest_distance = sys.maxsize
    
    # print(len(starts))
    
    for start in starts:
        cur_dist = search(start, end, input, input_clone)
        if cur_dist != -1:
            lowest_distance = min(lowest_distance, cur_dist)
    
    return lowest_distance

def entry():
    print("2022:Day12")
    input = parseInput("day12_input.txt")
    input2 = parseInput("day12_input.txt")
    
    # uncomment below to submit part A
    # ansA = partA(input, input2)
    # print(ansA)
    # submit(1, ansA, 2022, 12, SESSION_ID, USER_AGENT)
    
    # uncomment below to submit part B
    ansB = partB(input, input2)
    print(ansB)
    submit(2, ansB, 2022, 12, SESSION_ID, USER_AGENT)

if __name__=="__main__":
    entry()