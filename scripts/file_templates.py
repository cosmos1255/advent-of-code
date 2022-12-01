SINGLE_DAY_PYTHON_SCRIPT = """\"\"\"Advent of Code {YEAR}, Day: {DAY}
Author: David Eyrich
Link: https://adventofcode.com/{YEAR}/day/{DAY}\"\"\"

import os
import sys

scripts_path = os.getcwd()
scripts_path_split = scripts_path.split('/')
scripts_path_join = '/'.join(scripts_path_split[:-2])
sys.path.append(f"{scripts_path_join}/scripts")

from scripts.submit_ans import submit

def parseInput(filename):
    # read in from a file
    with open(filename, 'r') as f:
        input = f.read()
    
    # parse through input here
    parsedInput = ''
    
    return parsedInput

def partA(input):
    print("Part A")
    return 0

def partB(input):
    print("Part B")
    return 0

def entry():
    print("entry")
    input = parseInput("../input/day{DAY}_input.txt")
    
    # uncomment below to submit part A
    # ansA = partA(input)
    # submit(1, ansA, {YEAR}, {DAY})
    
    # uncomment below to submit part B
    # andB = partB(input)
    # submit(2, ansB, {YEAR}, {DAY})

if __name__=="__main__":
    entry()"""