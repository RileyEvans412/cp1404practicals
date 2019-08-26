"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Impossible")
    elif 90 > score > 49:
        print("Passable")
    if 90 <= score < 101:
        print("Excellent")
    if score < 50:
        print("Bad")