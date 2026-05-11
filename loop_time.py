n=10

for i in range(n):
    print(i)

for i in range(n):
    for j in range(n):
        print(i, j)

i = 1
while i < n:
    i *= 2
    print(i)