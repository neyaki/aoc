#!/usr/bin/env python3.10

"""
Author:         @neyaki
Date:           03 December 2022
Description:    Day 3 of the Advent of Code event puzzle: Rucksack Reorganization
Source:         https://adventofcode.com/2022/day/3
"""


# do the math
def elphabet_value(lett):
    if lett.islower():
        return ord(lett)-96
    else:
        return ord(lett.lower())-70


# variables
prioritysum1 = 0  # part 1
prioritysum2 = 0  # part 2

# read input and calculate
with open('day3.txt', 'r') as aoc_input:
    # part 1
    for line in aoc_input:
        for letter in line[:int(len(line.rstrip())/2)]:
            # compare letters by compartment (line in half, compare left -> right)
            if letter in line[int(len(line.rstrip())/2):]:
                prioritysum1 += elphabet_value(letter)
                break # only need to find first instance

    # part 2
    # rewind the cursor
    aoc_input.seek(0)
    lines = aoc_input.read().splitlines()
    # create pairs of the first three lines
    pairs = zip(lines[0::3], lines[1::3], lines[2::3])
    for pair in pairs:
        # get the common letter
        letter2 = (next((x for x in pair[0] if x in pair[1] and x in pair[2]), False))
        prioritysum2 += elphabet_value(letter2)

# output
print("The sum of the priorities #1 is:", prioritysum1) # part 1
print("The sum of the priorities #2 is:", prioritysum2) # part 2
