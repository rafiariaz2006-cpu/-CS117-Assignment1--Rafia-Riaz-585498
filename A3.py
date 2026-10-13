#A3
#colour coding of resistors
colour = input("Enter band colour: ").strip().lower()

if colour == "black":
    print("digit = 0")
elif colour == "brown":
   print("digit = 1")
elif colour == "red":
    print("digit = 2")
elif colour == "orange":
    print("digit = 3")
elif colour == "yellow":
    print("digit = 4")
elif colour == "green":
    print("digit = 5")
elif colour == "blue":
    print("digit = 6")
elif colour == "violet":
    print("digit = 7")
elif colour == "grey" or colour == "gray":
    print("digit = 8")
elif colour == "white":
    print("digit = 9")
else:
    print("invalid colour")

