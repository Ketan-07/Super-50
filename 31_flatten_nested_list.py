# Flatten a Nested List

# Type_01 : Using Nested for loop

numbers = [[1, 2], [3, 4], [5, 6]]
result=[]
for sublist in numbers:
    for num in sublist:
        result.append(num)

print(result)

# Type_02 : Using List Comprehension
numbers = [[1, 2], [3, 4], [5, 6]]
result=[num for sublist in numbers for num in sublist ]
print(result)

# Type_03 : Using nested list and numbers as values

numbers = [1, [2, 3], [4, [5, 6]], 7]

def flatten(numbers):
    result = []

    for item in numbers:
        if type(item) == list:
            result += flatten(item)
        else:
            result.append(item)

    return result

print(flatten(numbers))