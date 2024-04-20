"""Advent of Code 2023, Day: 2
Author: David Eyrich
Link: https://adventofcode.com/2023/day/2"""

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
    games = input.split('\n')
    
    for i, game in enumerate(games):
        tmp = game.replace(f'Game {i+1}: ', '')
        games[i] = tmp.split('; ')
        for j, round in enumerate(games[i]):
            games[i][j] = round.split(', ')
            for k, pull in enumerate(games[i][j]):
                val, color = pull.split(' ')
                games[i][j][k] = {'VAL': int(val), "COLOR": color}

    return games

def isGameGood(game, red, green, blue):
    
    target = {'red': red, 'green': green, 'blue': blue}
    r = g = b = 0
    
    for round in game:
        for pull in round:
            if (pull['COLOR'] == 'red'):
                r += pull['VAL']
                if (target['red'] < r):
                    return -1
            if (pull['COLOR'] == 'green'):
                g += pull['VAL']
                if (target['green'] < g):
                    return -1
            if (pull['COLOR'] == 'blue'):
                b += pull['VAL']
                if (target['blue'] < b):
                    return -1
        # print(r,g,b)
        r = g = b = 0
    
    return 0
        
def minCubes(game):
    target = {'red': 0, 'green': 0, 'blue': 0}
    r = g = b = 0
    
    for round in game:
        for pull in round:
            if (pull['COLOR'] == 'red'):
                r += pull['VAL']
                if (target['red'] < r):
                    target['red'] = r
            if (pull['COLOR'] == 'green'):
                g += pull['VAL']
                if (target['green'] < g):
                    target['green'] = g
            if (pull['COLOR'] == 'blue'):
                b += pull['VAL']
                if (target['blue'] < b):
                    target['blue'] = b
        # print(r,g,b)
        r = g = b = 0
        
    return target['red'] * target['blue'] * target['green']

def partA(input):
    print("Part A")
    
    """[input] takes the form of input/games[game[rounds[pulls]]]
    where:
        games/input: the entire set;
        game: one single game;
        round: one set of pulls;
        pull: num cubes of specific color (VAL/COLOR)"""
    
    sum = 0
    
    for i, game in enumerate(input):
        if isGameGood(game, 12, 13, 14) == 0:
            sum += i+1
    
    
    return sum

def partB(input):
    print("Part B")
    
    sum = 0
    
    for game in input:
        sum += minCubes(game)
    
    return sum

def entry():
    print("2023:Day2")
    input = parseInput("day2_input.txt")
    
    # uncomment below to submit part A
    ansA = partA(input)
    print(ansA)
    # submit(1, ansA, 2023, 2, SESSION_ID, USER_AGENT)
    
    # uncomment below to submit part B
    ansB = partB(input)
    print(ansB)
    submit(2, ansB, 2023, 2, SESSION_ID, USER_AGENT)

if __name__=="__main__":
    entry()