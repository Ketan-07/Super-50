numbers = [10, 50, 20, 80, 30]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print(largest)