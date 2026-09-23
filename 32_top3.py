# Find top 3 largest numbers

# Type_01 : Using Mannual Sorting
numbers = [10, 50, 20, 80, 30, 70]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] < numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(numbers[:3])

# Type_02 : set() + sorted()

numbers = [10, 50, 20, 80, 30, 70]

result = sorted(set(numbers), reverse=True)[:3]

print(result)