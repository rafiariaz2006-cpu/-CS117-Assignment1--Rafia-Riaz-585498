#C2
#PARALLEL RESISTANCE
def parallel_resistance(resistors):
    total = 0

    for r in resistors:
        total = total + (1 / r)

    return 1 / total


print("Parallel resistance =", parallel_resistance([10, 10]))
print("Parallel resistance =", round(parallel_resistance([100, 200, 300]), 2))
