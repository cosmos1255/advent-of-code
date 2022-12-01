SINGLE_DAY_PYTHON_SCRIPT = """\"\"\"Advent of Code {YEAR}, Day: {DAY}
Author: David Eyrich
Link: https://adventofcode.com/{YEAR}/day/{DAY}\"\"\"

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

def main():
    print("Main")
    input = parseInput("../input/day{DAY}_input.txt")
    
    # uncomment below to submit part A
    # ansA = partA(input)
    # submit(1, ansA, {YEAR}, {DAY})
    
    # uncomment below to submit part B
    # andB = partB(input)
    # submit(2, ansB, {YEAR}, {DAY})"""