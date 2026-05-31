# Input two numbers
num1 = int(input("Enter Largest number: "))
num2 = int(input("Enter Smallest number: "))

# Find the greater number
greater = max(num1, num2)

while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1

print("LCM is :", lcm)