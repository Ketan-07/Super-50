numbers = [10, 25, 5, 40, 15]

#Type_01 : using max() function
print(max(numbers))

#Type_02 : using loop
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)

#Type_03 : using sort() function
numbers.sort()
print(numbers[-1])