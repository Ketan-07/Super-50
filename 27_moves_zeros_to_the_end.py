# Type_01 : Using List Comprehension
numbers = [0, 1, 0, 3, 12]

result = [x for x in numbers if x != 0]
result += [0] * (len(numbers) - len(result))

print(result)

# Type_02 : Using For Loop

numbers = [0, 1, 0, 3, 12]
result = []

for num in numbers:
    if num != 0:
        result.append(num)

while len(result) < len(numbers):
    result.append(0)

print(result)

# Type_03 : Using Two Pointer

numbers = [0, 1, 0, 3, 12]
j=0

for i in range(len(numbers)):
    if numbers[i] != 0:
        numbers[j], numbers[i] = numbers[i], numbers[j]
        j += 1

print(numbers)