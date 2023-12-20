"""Advent of Code 2023, Day: 5
Author: David Eyrich
Link: https://adventofcode.com/2023/day/5"""

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
    input = input.split('\n')
    
    input[0] = input[0].replace("seeds: ", "")
    seeds = input[0].split(' ')
    one = two = thr = four = five = six = seven = 0
    se2so = []
    so2f = []
    f2w = []
    w2li = []
    li2t = []
    t2h = []
    h2lo = []
    
    for i in range(2, len(input)):
        if input[i] == '':
            one = two = thr = four = five = six = seven = 0
            continue
        elif input[i].__contains__("seed-to-soil"):
            one = 1
        elif input[i].__contains__("soil-to-fert"):
            two = 1
        elif input[i].__contains__("fertilizer-to-water"):
            thr = 1
        elif input[i].__contains__("water-to-light"):
            four = 1
        elif input[i].__contains__("light-to-temp"):
            five = 1
        elif input[i].__contains__("temperature-to-humid"):
            six = 1
        elif input[i].__contains__("humidity-to-loc"):
            seven = 1
        else:
            if (one):
                se2so.append(input[i].split(' '))    
            elif (two):
                so2f.append(input[i].split(' '))    
            elif (thr):
                f2w.append(input[i].split(' '))    
            elif (four):
                w2li.append(input[i].split(' '))    
            elif (five):
                li2t.append(input[i].split(' '))    
            elif (six):
                t2h.append(input[i].split(' '))    
            elif (seven):
                h2lo.append(input[i].split(' '))    
        
    parsed_input = [seeds, se2so, so2f, f2w, w2li, li2t, t2h, h2lo]
    # print(parsed_input)
    
    return parsed_input

def findNumber(value, dest, src, rang):
    
    if (value >= src and value <= src+rang):
        return (value-src)+dest
    return -1

    """For input argument: (1-7 take the form of [dest,src,rang_len])
        0: seeds
        1: seeds to soil
        2: soil to fertilizer
        3: fertilizer to water
        4: water to light
        5: light to temperature
        6: temperature to humidity
        7: humidity to location
    """ 
def partA(input):
    print("Part A")
    
    seeds, se2so, so2f, f2w, w2li, li2t, t2h, h2lo = input
    num = 0
    lowest = sys.maxsize
    
    for seed in seeds:
        num = int(seed)
        
        # print("seed: ", num)
        
        # find soil number
        for val in se2so:
            dest, src, rang = val
            snum = findNumber(num, int(dest), int(src), int(rang))
            if snum != -1:
                break
        if snum == -1:
            snum = num
        # print("soil: ", snum)
        # find fert number
        for val in so2f:
            dest, src, rang = val
            fnum = findNumber(snum, int(dest), int(src), int(rang))
            if fnum != -1:
                break   
        if fnum == -1:
            fnum = snum
        # print("fert: ", fnum)
        # find water number
        for val in f2w:
            dest, src, rang = val
            wnum = findNumber(fnum, int(dest), int(src), int(rang))
            if wnum != -1:
                break   
        if wnum == -1:
            wnum = fnum
        
        # print("water: ", wnum)
        # find light number
        for val in w2li:
            dest, src, rang = val
            linum = findNumber(wnum, int(dest), int(src), int(rang))
            if linum != -1:
                break   
        if linum == -1:
            linum = wnum
        # print("light: ", linum)
        # find temp number
        for val in li2t:
            dest, src, rang = val
            tnum = findNumber(linum, int(dest), int(src), int(rang))
            if tnum != -1:
                break   
        if tnum == -1:
            tnum = linum
        # print("temp: ", tnum)
        # find humid number
        for val in t2h:
            dest, src, rang = val
            hnum = findNumber(tnum, int(dest), int(src), int(rang))
            if hnum != -1:
                break   
        if hnum == -1:
            hnum = tnum
        # print("humid: ", hnum)
        # find location number
        for val in h2lo:
            dest, src, rang = val
            lonum = findNumber(hnum, int(dest), int(src), int(rang))
            if lonum != -1:
                break   
        if lonum == -1:
            lonum = hnum
        # print("loc: ", lonum)
        lowest = min(lowest, lonum)
    
    return lowest

def partB(input):
    print("Part B")
    
    seeds, se2so, so2f, f2w, w2li, li2t, t2h, h2lo = input
    num = 0
    lowest = sys.maxsize
    
    for i in range(len(seeds)-1):
        
        for num in range(int(seeds[i]), int(seeds[i])+int(seeds[i+1])+1):
        
            print("seed: ", num)
            
            # find soil number
            for val in se2so:
                dest, src, rang = val
                snum = findNumber(num, int(dest), int(src), int(rang))
                if snum != -1:
                    break
            if snum == -1:
                snum = num
            print("soil: ", snum)
            # find fert number
            for val in so2f:
                dest, src, rang = val
                fnum = findNumber(snum, int(dest), int(src), int(rang))
                if fnum != -1:
                    break   
            if fnum == -1:
                fnum = snum
            print("fert: ", fnum)
            # find water number
            for val in f2w:
                dest, src, rang = val
                wnum = findNumber(fnum, int(dest), int(src), int(rang))
                if wnum != -1:
                    break   
            if wnum == -1:
                wnum = fnum
            
            print("water: ", wnum)
            # find light number
            for val in w2li:
                dest, src, rang = val
                linum = findNumber(wnum, int(dest), int(src), int(rang))
                if linum != -1:
                    break   
            if linum == -1:
                linum = wnum
            print("light: ", linum)
            # find temp number
            for val in li2t:
                dest, src, rang = val
                tnum = findNumber(linum, int(dest), int(src), int(rang))
                if tnum != -1:
                    break   
            if tnum == -1:
                tnum = linum
            print("temp: ", tnum)
            # find humid number
            for val in t2h:
                dest, src, rang = val
                hnum = findNumber(tnum, int(dest), int(src), int(rang))
                if hnum != -1:
                    break   
            if hnum == -1:
                hnum = tnum
            print("humid: ", hnum)
            # find location number
            for val in h2lo:
                dest, src, rang = val
                lonum = findNumber(hnum, int(dest), int(src), int(rang))
                if lonum != -1:
                    break   
            if lonum == -1:
                lonum = hnum
            print("loc: ", lonum)
            print()
            lowest = min(lowest, lonum)
    
    return lowest

def entry():
    print("2023:Day5")
    input = parseInput("day5_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2023, 5, SESSION_ID, USER_AGENT)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    # submit(2, ansB, 2023, 5, SESSION_ID, USER_AGENT)

if __name__=="__main__":
    entry()