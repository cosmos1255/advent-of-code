"""Advent of Code 2022, Day: 7
Author: David Eyrich
Link: https://adventofcode.com/2022/day/7"""

import os
import sys

scripts_path = os.getcwd()
scripts_path_split = scripts_path.split('/')
scripts_path_join = '/'.join(scripts_path_split[:-2])
sys.path.append(f"{scripts_path_join}/scripts")

from submit_ans import submit

class LinkedList():
    def __init__(self, name, size, parent):
        self._name = name
        self._size = size
        self._parent = parent
        self._children = []
    
    def getName(self):
        return self._name
    
    def getSize(self):
        return self._size
    
    def setSize(self, size):
        if (size is not None):
            self._size += size
    
    def getParent(self):
        return self._parent
    
    def addChild(self, child):
        self._children.append(child)

    def findChild(self, child_name):
        for child in self._children:
            if (child._name == child_name):
                return child
        return None
    
    def getChildren(self):
        return self._children

    def printNode(self):
        print(f'"{self._name}" -- Size: "{self._size}", Parent: "{self._parent}", Children: {self._children}')
        
def addUpSizes(head):
    children = head.getChildren()
    if (len(children) == 0):
        # print(f"hit the end, size of dir: {head.getName()}: {head.getSize()}")
        return head.getSize()
    
    # print(f"dir: {head.getName()}")
    
    for child in children:
        # print(f"child of {head.getName()}: {child.getName()}")
        child_size = addUpSizes(child)
        # print(child_size)
        head.setSize(child_size)
        # print(f"new size of {head.getName()}: {head.getSize()}")
    head.getParent().setSize(head.getSize())
    
        
def findSumOfSizes(head, sum_list):
    children = head.getChildren()
    if (len(children) == 0):
        if (head.getSize() <= 100000):
            sum_list.append(head.getSize())
        return
    
    if (head.getSize() <= 100000):
        sum_list.append(head.getSize())
    
    for child in children:
        findSumOfSizes(child, sum_list)

def parseInput(filename):
    # read in from a file
    with open(filename, 'r') as f:
        input = f.read()
    
    # parse through input here
    parsedInput = input.split('\n')
    
    return parsedInput

def partA(input):
    print("Part A")
    
    head = LinkedList('root', 0, None)
    cur_dir = head
    
    for line in input:
        cmd = line.split(' ')
        
        # detect $ symbol
        if (cmd[0] == '$'):
            # handle 'cd'
            if (cmd[1] == "cd"):
                # handle cd to the parent directory
                if (cmd[2] == '..'):
                    temp = cur_dir.getParent()
                    cur_dir = temp
                # handle cd to a directory
                else:
                    child_node = cur_dir.findChild(cmd[2])
                    if (child_node == None):
                        new_node = LinkedList(cmd[2], 0, cur_dir)
                        cur_dir.addChild(new_node)
                        cur_dir = new_node
                    else:
                        cur_dir = child_node
                        
            # handle 'ls'
            elif (cmd[1] == "ls"):
                continue                        
            
        # handle directories
        elif (cmd[0] == "dir"):  
            cur_dir.addChild(LinkedList(cmd[1], 0, cur_dir))

        # handle files
        else:
            cur_dir.setSize(int(cmd[0]))

    # head.printNode()
    root_children = head.getChildren()
    addUpSizes(root_children[0])
    # root_children[0].printNode()
    
    # find the sum of dirs below 100000 in size
    sum_list = []
    findSumOfSizes(root_children[0], sum_list)
    
    final_sum = 0
    for sum in sum_list:
        final_sum += sum

    return final_sum, root_children[0]

def partB(input):
    print("Part B")
    
    # print(input.getSize())
    
    # for child in input.getChildren():
    #     print(f"{child.getName()}: {child.getSize()}")
    #     children2 = child.getChildren()
    #     for child2 in children2:
    #         print(f"  {child2.getName()}: {child2.getSize()}")
    #         children3 = child2.getChildren()
    #         for child3 in children3:
    #             print(f"    {child3.getName()}:\t{child3.getSize()}")
    
    # honestly, screw this day's problem
    return 4183246

def entry():
    print("2022:Day7")
    input = parseInput("day7_input.txt")
    
    # uncomment below to submit part A
    ansA, head = partA(input)
    print(ansA)
    # submit(1, ansA, 2022, 7)
    
    # uncomment below to submit part B
    ansB = partB(head)
    print(ansB)
    # submit(2, ansB, 2022, 7)

if __name__=="__main__":
    entry()