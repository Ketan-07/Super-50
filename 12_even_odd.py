#Type_01 : Using for loop
numbers = [10, 15, 22, 7, 8, 13]

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)

#Type_02 : Using list Comprehension
numbers = [10, 15, 22, 7, 8, 13]

even = [num for num in numbers if num % 2 == 0]
odd = [num for num in numbers if num % 2 != 0]

print("Even:", even)
print("Odd:", odd)

#Type_03 : Using filter()
numbers = [10, 15, 22, 7, 8, 13]

even = list(filter(lambda num: num % 2 == 0, numbers))
odd = list(filter(lambda num: num % 2 != 0, numbers))

print("Even:", even)
print("Odd:", odd)