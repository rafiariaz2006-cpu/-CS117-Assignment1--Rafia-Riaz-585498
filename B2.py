#B2
#Resistor in series
count = int(input("How many resistors? "))
total_resistance = 0.0

for index in range(1, count + 1):
    print("Enter resistance number", index)
    resistance = float(input())
    total_resistance += resistance

print("Total resistance =", total_resistance, "ohm")
