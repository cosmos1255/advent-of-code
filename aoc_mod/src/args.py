import argparse

def aoc_mod_parse_args():
    # set up argparser to handle input if needed
    args = argparse.ArgumentParser(add_help=True)
    
    args.add_argument('-y', help='Enter the year of the Advent of Code challenge you would like.')
    args.add_argument('-d', help='Enter the day of the Advent of Code challenge you would like.')
    
    return args.parse_args()