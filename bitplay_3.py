
# Step 1: Swap Without a Third Variable
a = 10
b = 20

print("Before swapping: a =", a, ", b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)

# Step 2: Perform XOR Swap
x = 5
y = 15

print("\nBefore XOR swap: x =", x, ", y =", y)

x = x ^ y
y = x ^ y
x = x ^ y

print("After XOR swap: x =", x, ", y =", y)

# Step 3: Use Left Shift to Double Numbers
num = 6

print("\nOriginal number:", num)
print("Number doubled:", num << 1)
print("Number multiplied by 4:", num << 2)

# Step 4: Detect Different Signs with XOR
num1 = -8
num2 = 12

if (num1 < 0) ^ (num2 < 0):
    print("\nThe numbers have different signs.")
else:
    print("\nThe numbers have the same sign.")

# Step 5: Divide Without Using /
dividend = 17
divisor = 5
quotient = 0
remainder = dividend

if divisor == 0:
    print("\nCannot divide by zero.")
else:
    while remainder >= divisor:
        remainder = remainder - divisor
        quotient = quotient + 1

    print("\nDividend:", dividend)
    print("Divisor:", divisor)
    print("Quotient:", quotient)
    print("Remainder:", remainder)
