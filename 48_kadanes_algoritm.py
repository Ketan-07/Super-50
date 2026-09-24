numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current = numbers[0]
maximum = numbers[0]

for i in range(1, len(numbers)):
    current = max(numbers[i], current + numbers[i])
    maximum = max(maximum, current)

print(maximum)