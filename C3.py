#C3
#decimal to binary
def decimal_to_binary(n):
    binary = ""

    while n > 0:
        remainder = n % 2
        binary = str(remainder) + binary
        n = n // 2

    return binary


print("Binary of 15 =", decimal_to_binary(15))
print("Binary of 20 =", decimal_to_binary(20))
