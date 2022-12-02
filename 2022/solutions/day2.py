#!/usr/bin/env python3.10

"""
Author:         @neyaki
Date:           02 December 2022
Description:    Day 2 of the Advent of Code event puzzle: Rock Paper Scissors
Source:         https://adventofcode.com/2022/day/2
"""

# ROCK = A, X
# PAPER = B, Y
# SCISSORS = C, Z

# read input
elfsturn = []
yourturn_or_results = []
with open('day2.txt', 'r') as aoc_input:
    for line in aoc_input:
        (elf, you) = line.split()
        elfsturn.append(elf)
        yourturn_or_results.append(you)


# rules
# part 1
elfrules = {"A": "Z", "B": "X", "C": "Y", "X": "C", "Y": "A", "Z": "B"}
# part 2
# X = LOSE
loserules = {"A": "Z", "B": "X", "C": "Y"}
# Y = DRAW
drawrules = {"A": "X", "B": "Y", "C": "Z"}
# Z = WIN
reversedrules = dict(map(reversed, elfrules.items()))

# scoring
# part 1
elfscoring = {"X": 1, "Y": 2, "Z": 3}
totscore = 0
# part 2
tot2score = 0

# do the math
for round in range(len(elfsturn)):
    # part 1
    if elfrules[elfsturn[round]] == yourturn_or_results[round]:
        totscore += elfscoring[yourturn_or_results[round]]
    elif elfrules[yourturn_or_results[round]] == elfsturn[round]:
        totscore += (elfscoring[yourturn_or_results[round]] + 6)
    else:
        totscore += (elfscoring[yourturn_or_results[round]] + 3)
    # part 2
    match yourturn_or_results[round]:
        case "X":
            tot2score += elfscoring[loserules[elfsturn[round]]]
        case "Y":
            tot2score += (elfscoring[drawrules[elfsturn[round]]] + 3)
        case "Z":
            tot2score += (elfscoring[reversedrules[elfsturn[round]]] + 6)

print("total rounds: " + str(len(elfsturn)))
print("total score #1: " + str(totscore))
print("total score #2: " + str(tot2score))
