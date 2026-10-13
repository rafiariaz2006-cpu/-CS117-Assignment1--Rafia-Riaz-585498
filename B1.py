#B1
#ohm's law table
resistance = 3

for voltage in range(1, 11):
    current = voltage / resistance
    print("V =", voltage, "V, I =",(current), "A")
