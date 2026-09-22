# Find duplicate elements
numbers = [1,2,3,4,3,2,1,5]
duplicate = []
for i in numbers:
    if numbers.count(i) > 1 and i not in duplicate:
        duplicate.append(i)

print(duplicate)