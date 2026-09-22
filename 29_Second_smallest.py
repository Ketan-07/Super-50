# Find second smallest number

# Type_01 : Using for loop

numbers = [10, 5, 20, 5, 2]
min_1 = numbers[0]
min_2 = numbers[0]

for num in numbers:
    if num < min_1:
        min_2 = min_1
        min_1 = num
    elif num < min_2 and num != min_1:
        min_2 = num

print(min_2)

# Type_02 : Using Sorted

numbers = [10, 5, 20, 5, 2]

unique = sorted(set(numbers))

print(unique[1])