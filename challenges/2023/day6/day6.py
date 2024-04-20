"""Advent of Code 2023, Day: 6
Author: David Eyrich
Link: https://adventofcode.com/2023/day/6"""

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
        input = f.readlines()
    
    # parse through input here
    parsedInput = '' 
    
    times = input[0].strip('\n').split(':')[1].split(' ')
    distances = input[1].strip('\n').split(':')[1].split(' ')

    times = [i for i in times if i != ''] 
    distances = [i for i in distances if i != ''] 
    
    
    # print(times, distances)
    
    return times, distances

def calculate_dist(speed, time):
    return speed*time

# input structure (times, distances)
def partA(input):
    print("Part A")
    
    ts, ds = input
    
    ts = [int(i) for i in ts]
    ds = [int(i) for i in ds]
    
    counts = []
    curr_cnt = 0
    product_res = 1
    
    for t, d in zip(ts, ds):
        for i in range(1, t):
            if calculate_dist(i, t-i) > d:
                curr_cnt += 1
        
        counts.append(curr_cnt)
        curr_cnt = 0
    
    for val in counts:
        product_res *= val
    
    return product_res

# input structure (times, distances)
def partB(input):
    print("Part B")
    
    ts, ds = input
    
    ts = int(''.join(ts))
    ds = int(''.join(ds))
    
    for i in range(1, ts):
        if calculate_dist(i, ts-i) > ds:
            # print(i, ": ", calculate_dist(i, ts-i))
            break
        
    for j in reversed(range(1, ts)):
        if calculate_dist(j, ts-j) > ds:
            # print(j, ": ", calculate_dist(j, ts-j))
            break
        
    return j-i+1

def entry():
    print("2023:Day6")
    input = parseInput("day6_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2023, 6, SESSION_ID, USER_AGENT)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    submit(2, ansB, 2023, 6, SESSION_ID, USER_AGENT)

if __name__=="__main__":
    entry()