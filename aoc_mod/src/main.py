#!/usr/bin/env python3
"""Script to initialize a new day for Advent of Code.
This script will basically grab the input and puzzle clue
from the Advent of Code website.

If user specifies a year and day, this script will create
the files pertaining to that day and year.

Author: David Eyrich
"""

import time
import requests
from argparse import aoc_mod_parse_args
import os
from request_data import USER_AGENT, SESSION_ID
from file_templates import SINGLE_DAY_PYTHON_SCRIPT
    
def getCurTime():
    cur_time = time.time()
    ts = time.localtime(cur_time)
    return ts

def parseYearDay(str_year, str_day):
    cur_time = getCurTime()
    max_year = cur_time.tm_year
    
    int_year = int(str_year)
    int_day = int(str_day)
    
    # check for the proper year (2015 and up)
    if (int_year < 2015 or int_year > max_year):
        if (int_year == max_year):
            if (cur_time.tm_mon != 12):
                print("It's not quite time for this script to be run. Please wait until December!")
                exit(0)
            elif (cur_time.tm_mday < int_day):
                print("Can't get data from the future, try running the script again "
                        "with the proper input.")
                exit(0)
            else:
                return int_year, int_day
        else:
            print(f'Improper year entered, please try again. Advent of Code started in 2015.')
            exit(0)
    
    # if we are in the proper year, we need to check the correct day
    if (int_day < 1 or int_day > 25):
        print("Improper day entered, Advent of Code runs from December 1st to 25th.")
        exit(0)
    
    # if we get here, we have a valid day and year
    return int_year, int_day 

def grabData(year, day):
    URL = f'https://adventofcode.com/{year}/day/{day}/input'

    # grab input data
    input_req = requests.get(url=URL, cookies={'session': SESSION_ID, 'User-Agent': USER_AGENT})
    input_data = input_req.content
    
    return input_data
        
def checkDecember():
    cur_time = getCurTime()
    
    if (cur_time.tm_mon != 12):
        print("It's not quite time for this script to be run. Please wait until December!")
        exit(0)
    
    if (cur_time.tm_mday > 25):
        print("Oh no! Christmas is over? Rerun the script with the proper input "
              "to get your Advent of Code challenge data!")    
        exit(0)
    
    # if we make it here, it is December 1st-25th of the proper year
    return cur_time.tm_year, cur_time.tm_mday

def entry():
    # for default values
    cur_time = getCurTime()
    cur_year, cur_day = cur_time.tm_year, cur_time.tm_mday
    
    opts = aoc_mod_parse_args()
    
    if (opts.y is not None):
        if (opts.d is not None):
            year, day = parseYearDay(opts.y, opts.d)
        else:
            print("ERROR: Both year and day are required to create challenge data.")
            exit(0)
    else:
        if (opts.d is not None):
            print("ERROR: Both year and day are required to create challenge data.")
            exit(0)
        else:
            # if we get here, no input was entered so we will 
            # check to see if the current year is available
            year, day = checkDecember()

    # grab the input data with the proper year and day
    data = grabData(year, day)
    
    # create proper files to be used
    day_path = f"{year}/day{day}"
    os.system(f"mkdir -p {day_path}")
    soln_path = f"{day_path}/day{day}.py"
    input_path = f"{day_path}/day{day}_input.txt"
    
    if (not os.path.exists(soln_path)):
        with open(soln_path, 'w') as f_soln:
            f_soln.write(SINGLE_DAY_PYTHON_SCRIPT.format(YEAR=year, DAY=day,
                                                        scripts_path_join="{scripts_path_join}"))
    else:
        print(f"{year}, Day {day} solution file already exists.")
        
    if (not os.path.exists(input_path)):
        with open(input_path, "wb") as f_input:
            f_input.write(data[:-1])
    else:
        print(f"{year}, Day {day} input file already exists.")
    
if __name__=="__main__":
    entry()