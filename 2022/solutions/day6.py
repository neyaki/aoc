#!/usr/bin/env python3.10

"""
Author:         @neyaki
Date:           06 December 2022
Description:    Day 6 of the Advent of Code event puzzle: Tuning Trouble
Source:         https://adventofcode.com/2022/day/6
"""


def find_unique_set(lst: list, set_size: int) -> int:
    for line in lst:
        pt = 0  # set pointer
        for l in line:
            if len(line[pt:pt+set_size]) == len(set(line[pt:pt+set_size])):
                return len(line[:pt+set_size])
            else:
                pt += 1


# read input (and calculate)
with open('day6.txt', 'r') as aoc_input:
    datastream = aoc_input.read().splitlines()


# output
# part 1 - find unique set of 4 in single datastream
print("part 1:", find_unique_set(datastream, 4))
# part 2 - find unique set of 14 in single datastream
print("part 2:", find_unique_set(datastream, 14))

