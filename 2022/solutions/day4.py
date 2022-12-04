#!/usr/bin/env python3.10

"""
Author:         @neyaki
Date:           04 December 2022
Description:    Day 4 of the Advent of Code event puzzle: Camp Cleanup
Source:         https://adventofcode.com/2022/day/4
"""

# variables
howmany1 = 0  # part 1
howmany2 = 0  # part 2

# read input and calculate part 1 & 2
with open('day4.txt', 'r') as aoc_input:
    for line in aoc_input:
        (assignmentL, assignmentR) = line.rstrip().split(",")
        # generate an inclusive range
        L = range(int(assignmentL.split("-")[0]),
                  int(assignmentL.split("-")[1])+1)
        R = range(int(assignmentR.split("-")[0]),
                  int(assignmentR.split("-")[1])+1)
        # provide the overlapping range numbers
        compared = range(max(L.start, R.start), min(L.stop, R.stop)) or None
        # part 1; calculate complete overlap
        # part 2; calculate complete and partial overlap
        if compared == L or compared == R:
            howmany1 += 1
            howmany2 += 1
        elif compared != None:
            howmany2 += 1

# output
print("In how many assignment pairs does one range fully contain the other?", howmany1)  # part 1
print("In how many assignment pairs do the ranges overlap?", howmany2)  # part 2
