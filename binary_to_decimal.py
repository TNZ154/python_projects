# Binary to Decimal Converter

binary = input("Enter a binary number: ")

decimal = 0
power = 0

# Start from the right side of the binary number
for digit in reversed(binary):
    decimal += int(digit) * (2 ** power)
    power += 1

print("Decimal number is:", decimal)