"""
CP1404/CP5632 Practical
Hex Colours
"""

COLOUR_TO_HEX = {"aliceblue": "#f0f8ff", "absolute zero": "#0048ba", "banana yellow": "#ffe135", "beaver": "#9f8170",
                 "battleship gray": "#848482", "blueviolet": "#8a2be2", "cameo pink": "#efbbcc", "canary": "#ffff99",
                 "candy pink": "#e4717a", "dark brown": "#654321"}

colour = input("Please enter a colour: ").lower()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_HEX[colour])
    except KeyError:
        print("Invalid Colour")
    colour = input("Please enter a colour: ").lower()
