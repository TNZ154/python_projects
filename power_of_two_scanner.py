# Power of Two Scanner

n = int(input("Enter a number: "))

# Check if n is a power of 2
if n > 0 and (n & (n - 1)) == 0:
    print(n, "is a power of 2")
else:
    print(n, "is not a power of 2")

# Remove the rightmost set bit
result = n & (n - 1)
print("After removing the rightmost set bit:", result)