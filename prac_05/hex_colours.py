"""
CP1404/CP5632 Practical
State hexadecimal colour code
Invalid names shouldn't crash
"""

HEX_COLOURS = {"blue violet": "#8a2be2", "chocolate": "#d2691e", "coral": "#ff7f50", "dark goldenrod": "#b8860b",
               "dark green": "#006400", "dark orange": "#ff8c00", "lawn green": "#7cfc00", "linen": "#faf0e6",
               "medium": "#66cdaa", "mint cream": "#f5fffa"}

user_colour = input("Please enter a colour name: ").lower()
while user_colour != "":
    if user_colour in HEX_COLOURS:
        print(user_colour + "'s colour code is " + HEX_COLOURS[user_colour])
    else:
        print("Invalid colour: ")
    user_colour = input("Please enter a colour name: ").lower()

