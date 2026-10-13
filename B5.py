#B5
#resistor tolerance sorting
one_percent = 0
five_percent = 0
reject = 0

while True:
    resistance = float(input("Enter measured resistance (0 to stop): "))

    if resistance == 0:
        break

    if 99.0 <= resistance <= 101.0:
        one_percent += 1
    elif 95.0 <= resistance <= 105.0:
        five_percent += 1
    else:
        reject += 1

print("1% tolerance:", one_percent)
print("5% tolerance:", five_percent)
print("Reject:", reject)
