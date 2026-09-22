numbers = [10, 5, 20, 2, 30]

smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n

print(smallest)