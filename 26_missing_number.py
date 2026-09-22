# Type_01 : Using Sum Formula
numbers = [1, 2, 3, 5, 6]

n = 6

missing = n * (n + 1) // 2 - sum(numbers)

print(missing)

# Type_02 : For loop
numbers = [1, 2, 3, 5, 6]
n = 6

missing = 0

for i in range(1, n + 1):
    if i not in numbers:
        missing = i
        break

print(missing)