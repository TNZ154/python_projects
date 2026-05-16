def prints(n):
    if n <= 0:
        return
    print("Codingal")
    prints(n // 2)
    prints(n // 2)
prints(8)
print("O(1)")
print("O(log n)")
print("\n")

def sum_n(n):
    return n * (n + 1) // 2 #Integer result
print("Sum of first n numbers (n=5):", sum_n(5))
print("O(1)")
print("O(1)")
print("\n")

def array_sum(a):
    total = 0
    for num in a:
        total += num
    return total
a = [12, 3, 4, 15]
print("Array sum:", array_sum(a))
print("O(n)")
print("O(1)")
print("\n")

def summ(n):
    if n <= 0:
        return 0
    return n + summ(n - 1)
print("Recursive sum (n=5):", summ(5))
print("O(1)")
print("O(n)")
print("\n")