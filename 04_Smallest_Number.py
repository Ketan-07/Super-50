numbers = [10, 25, 5, 40, 15]

#Type_01 : using min() function
print(min(numbers))

#Type_02 : using loop
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)

#Type_03 : using sort() function
numbers.sort()
print(numbers[0])