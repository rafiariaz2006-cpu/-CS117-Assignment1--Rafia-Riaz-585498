#C1
#current and power
def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return i * i * r

voltage = 20
resistance = 5

current = ohms_current(voltage, resistance)
power = power_dissipated(current, resistance)

print("Current =", current, "A")
print("Power =", power, "W")
