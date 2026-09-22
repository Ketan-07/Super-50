# Find common elements in two lists
# Type_01 : Using set intersection

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = list(set(list1) & set(list2))

print(common)

# Type_02 : Using for loop

list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

common = []

for num in list1:
    if num in list2 and num not in common :
        common.append(num)

print(common)