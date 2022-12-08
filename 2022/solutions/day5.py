#!/usr/bin/env python3.10

"""
Author:         @neyaki
Date:           05 December 2022
Description:    Day x of the Advent of Code event puzzle: Stacks
Source:         https://adventofcode.com/2022/day/5
"""
import re
import typing
from collections import deque


# helpers
def lmap(func, *iterables):
    return list(map(func, *iterables))


def ints(s: str) -> typing.List[int]:
    return lmap(int, re.findall(r"-?\d+", s))


# read input
with open('day5.txt', 'r') as aoc_input:
    stacks_n_instructions = aoc_input.read().splitlines()

# get stacks
stacks = [stacks_n_instructions[: stacks_n_instructions.index("")],
          stacks_n_instructions[stacks_n_instructions.index("") + 1:]]

# get stack instructions
nrofboxes = []
startstack = []
endstack = []
for r in stacks[1]:
    nrofboxes.append(ints(r)[0])
    startstack.append(ints(r)[1])
    endstack.append(ints(r)[2])


# build the the stack columns
n = 4
r = 0
stackcolumns = [deque([]) for i in range(len(stacks[0]))]
for row in stacks[0]:
    col = 0
    boxlist = []
    if r == len(stacks[0])-1:
        break
    box_in_row = [row[i:i+n].strip() for i in range(0, len(row), n)]
    for box in box_in_row:
        col += 1
        if box == "":
            continue
        else:
            boxlist.append(box)
            stackcolumns[col-1].append(box)
    r += 1


# do the move
for x in range(len(stacks[1])):
    # part 1 - move single box at a time
    """for y in range(nrofboxes[x]):
        stackcolumns[endstack[x] -
                     1].appendleft(stackcolumns[startstack[x]-1][0])
        stackcolumns[startstack[x]-1].popleft() if True else None
    """
    # part 2 - move all boxes per move
    for y in range(nrofboxes[x], 0, -1):
        stackcolumns[endstack[x] -
                     1].appendleft(stackcolumns[startstack[x]-1][y-1])

    for y in range(nrofboxes[x]):
        stackcolumns[startstack[x]-1].popleft() if True else None


# output calculation (uncomment the part 1 section to use their values in below loop)
for val in range(len(stackcolumns)):
    print("stack", val+1, " top box", stackcolumns[val][0])
