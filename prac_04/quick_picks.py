"""
"Quick Picks" lottery Ticket Generator
Write a program that asks the user how many "Quick Picks" they wish to generate.
The program should generate the amount of lines of output that the user requested.
Each line consists of 6 random numbers between 1 and 45. The values 1 - 45 should be stored as constants
"""

import random
MIN_RANDOM = 1
MAX_RANDOM = 45

# ask for user input
number_of_picks = int(input("How many quick picks would you like: "))
# if the input is outside of max or min, request new input
while number_of_picks not in range(MIN_RANDOM, MAX_RANDOM + 1):
    number_of_picks = int(input("How many quick picks would you like: "))

# loops for the amount of requested picks
for pick in range(number_of_picks):
    # creates a list of picks and resets the list for every loop
    quick_picks = []
    # chooses a pick from 1 - 45, 6 times
    for picks in range(6):
        quick_pick = random.randint(MIN_RANDOM, MAX_RANDOM)
        while quick_pick in quick_picks:
            quick_pick = random.randint(MIN_RANDOM, MAX_RANDOM)
        quick_picks.append(quick_pick)
    print(sorted(quick_picks))
