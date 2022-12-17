"""Advent of Code 2022, Day: 9
Author: David Eyrich
Link: https://adventofcode.com/2022/day/9"""

import os
import sys
import math

scripts_path = os.getcwd()
scripts_path_split = scripts_path.split('/')
scripts_path_join = '/'.join(scripts_path_split[:-2])
sys.path.append(f"{scripts_path_join}/scripts")

from submit_ans import submit

def parseInput(filename):
    # read in from a file
    with open(filename, 'r') as f:
        input = f.readlines()
    
    # parse through input here
    parsedInput = []
    for i, x in enumerate(input): 
        parsedInput.append(x.strip('\n'))
    
    return parsedInput

def findDistance(H, T):
    dist = math.sqrt((H[0]-T[0])*(H[0]-T[0]) + (H[1]-T[1])*(H[1]-T[1]))
    print(int(dist))
    return int(dist)

def moveDiag(H, T):
    # move diag up, right
    if (H[0] > T[0] and H[1] > T[1]):
        T[0] += 1
        T[1] += 1
    # move diag down, right
    elif (H[0] > T[0] and H[1] < T[1]):
        T[0] += 1
        T[1] -= 1
    # move diag down, left
    elif (H[0] < T[0] and H[1] < T[1]):
        T[0] -= 1
        T[1] -= 1
    # move diag up, left
    elif (H[0] < T[0] and H[1] > T[1]):
        T[0] -= 1
        T[1] += 1
    else:
        print(f'uh... {H} -- {T}')
    return T

def partA(input):
    print("Part A")
    
    loc_H = [0,0]
    loc_T = [0,0]
    
    tail_visited = []
    tail_visited.append((loc_T[0], loc_T[1]))
    
    for cmd in input:
        print(f'{loc_H} -- {loc_T}')
        direction, dist = cmd.split(' ')
        dist = int(dist)
        
        if (direction == 'U'):
            loc_H[1] += dist
        elif (direction == 'D'):
            loc_H[1] -= dist
        elif (direction == 'L'):
            loc_H[0] -= dist
        elif (direction == 'R'):
            loc_H[0] += dist
             
        print(f'after H moves: {loc_H} -- {loc_T}')
        while (findDistance(loc_H, loc_T) > 1):
            # if T is not in same row/col as H, move diag 1
            if (loc_H[0] != loc_T[0] and loc_H[1] != loc_T[1]):
                loc_T = moveDiag(loc_H, loc_T)
            # else just move until we aren't greater than 1 away
            else:
                if (direction == 'U'):
                    loc_T[1] += 1
                elif (direction == 'D'):
                    loc_T[1] -= 1
                elif (direction == 'L'):
                    loc_T[0] -= 1
                elif (direction == 'R'):
                    loc_T[0] += 1
            
            # count up the visited nodes
            if (tail_visited.__contains__((loc_T[0], loc_T[1]))):
                print('visited')
                continue
            else:
                tail_visited.append((loc_T[0], loc_T[1]))
    
    return len(tail_visited)

def partB(input):
    print("Part B")
    return 0

def entry():
    print("2022:Day9")
    input = parseInput("day9_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 9)
    
    # uncomment below to submit part B
    # ansB = partB(input)
    # print(ansB)
    # submit(2, ansB, 2022, 9)

if __name__=="__main__":
    entry()