# Function using 1 iteration
def multiply_one_iteration(n, m):
    return n * m


# Function using N iterations
def multiply_n_iterations(n, m):
    result = 0

    for i in range(m):
        result = result + n

    return result


# User input
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))

# Function calls
print("Using 1 iteration:", multiply_one_iteration(n, m))
print("Using N iterations:", multiply_n_iterations(n, m))