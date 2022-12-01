#!/usr/bin/env python3.10

"""
Author:         @neyaki
Date:           01 December 2022
Description:    Day 1 of the Advent of Code event puzzle: Calorie Counting
Source:         https://adventofcode.com/2022/day/1
"""

# read input from a file
with open('day1.txt', 'r') as aoc_input:
    calories = aoc_input.read().splitlines()
    # add a whiteline at the end as delimeter
    calories.append("")
    totcal = 0
    totcalgroup = []
    for c in calories:
        if c == "":
            totcalgroup.append(totcal)
            totcal = 0
            continue
        else:
            totcal += int(c)

# part 1 - get highest calories
print("highest number is: " + str(max(totcalgroup)))

# part 2 - get top three's total calories
tottop3cal = 0
for topcal in sorted(totcalgroup, reverse=True)[:3]:
    tottop3cal += topcal

print("total for top 3 highest calories is: " + str(tottop3cal))
