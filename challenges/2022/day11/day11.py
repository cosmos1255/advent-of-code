"""Advent of Code 2022, Day: 11
Author: David Eyrich
Link: https://adventofcode.com/2022/day/11"""

import os
import sys
import re

scripts_path = os.getcwd()
scripts_path_split = scripts_path.split('/')
scripts_path_join = '/'.join(scripts_path_split[:-2])
sys.path.append(f"{scripts_path_join}/scripts")

from submit_ans import submit

def parseInput(filename):
    # read in from a file
    with open(filename, 'r') as f:
        input = f.read()
    
    input_split = input.split("Monkey ")
    input_split.remove('')
    pattern = r"[^: \n,]+"
    
    # parse through input here
    parsedInput = []
    for i in input_split:
        parsedInput.append(re.findall(pattern, i))
    
    monkeys = []
    for i, monkey in enumerate(parsedInput):
        monkeys.append({})
        
        item_i = monkey.index("items")
        op_i = monkey.index("Operation")
        test_i = monkey.index("Test")
        true_i = monkey.index("true")
        false_i = monkey.index("false")
        
        monkeys[i]['items'] = monkey[item_i+1:op_i]
        for j, item in enumerate(monkeys[i]['items']):
            monkeys[i]['items'][j] = int(item)
        monkeys[i]['operation'] = monkey[op_i+4:test_i]
        monkeys[i]['operation'][1] = monkeys[i]['operation'][1]
        monkeys[i]['test'] = int(monkey[test_i+3])
        monkeys[i]['true'] = int(monkey[true_i+4])
        monkeys[i]['false'] = int(monkey[false_i+4])
        monkeys[i]['inspected'] = 0
    
    return monkeys

def partA(input):
    print("Part A")
    num_rounds = 20
    for i in range(0, num_rounds):
        for j, monkey in enumerate(input):
            if (len(monkey['items']) == 0):
                continue
            for k, item in enumerate(monkey['items']):
                monkey['inspected'] += 1
                
                # test for the operation
                if (monkey['operation'][1].isalpha()):
                    op = item
                else:
                    op = int(monkey['operation'][1])
                
                # perform the operation
                if (monkey['operation'][0] == '*'):
                    monkey['items'][k] = int((item * op) / 3)
                else:
                    monkey['items'][k] = int((item + op) / 3)
                
                # perform the test
                if ((monkey['items'][k] % monkey['test']) == 0):
                    input[monkey['true']]['items'].append(monkey['items'][k])
                else:
                    input[monkey['false']]['items'].append(monkey['items'][k])
            monkey['items'] = []
                    
    num_inspected = []
    for monkey in input:
        num_inspected.append(monkey['inspected'])
    
    num_inspected.sort()

    return num_inspected[-1]*num_inspected[-2]

def partB(input):
    print("Part B")
    num_rounds = 10000
    
    mod_1 = 1
    for monkey in input:
        mod_1 *= monkey['test']
    print(mod_1)
    
    for i in range(0, num_rounds):
        for j, monkey in enumerate(input):
            if (len(monkey['items']) == 0):
                continue
            for k, item in enumerate(monkey['items']):
                monkey['inspected'] += 1
                
                # test for the operation
                if (monkey['operation'][1].isalpha()):
                    op = item
                else:
                    op = int(monkey['operation'][1])
                
                # perform the operation
                if (monkey['operation'][0] == '*'):
                    monkey['items'][k] = (item * op) % mod_1
                else:
                    monkey['items'][k] = (item + op) % mod_1
                
                # perform the test
                if ((monkey['items'][k] % monkey['test']) == 0):
                    input[monkey['true']]['items'].append(monkey['items'][k])
                else:
                    input[monkey['false']]['items'].append(monkey['items'][k])
            monkey['items'] = []
                    
    num_inspected = []
    for monkey in input:
        num_inspected.append(monkey['inspected'])
    
    num_inspected.sort()

    return num_inspected[-1]*num_inspected[-2]

def entry():
    print("2022:Day11")
    
    # uncomment below to submit part A
    input = parseInput("day11_input.txt")
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 11)
    
    # uncomment below to submit part B
    input = parseInput("day11_input.txt")
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2022, 11)

if __name__=="__main__":
    entry()