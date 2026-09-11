numbers = [10, 20, 40, 30, 50]

#Type_01 : using sort() function
unique = list(set(numbers))
unique.sort()

print(unique[-2])

#Type_02 : using loop
largest = 0
second_largest = 0

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)

#Type_03 : using max() and remove() function
largest = max(numbers)
numbers.remove(largest)
second_largest = max(numbers)
print(second_largest)