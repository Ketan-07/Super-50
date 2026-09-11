#Type_01 : Using set() function

numbers = [10, 20, 40, 30, 50, 10, 20, 30]
unique = list(set(numbers))
unique.sort()  #set() removes duplicates and returns a set object, which is then converted back to a list using list()
print(unique)


#Type_02 : Using loop
numbers = [10, 20, 40, 30, 50, 10, 20, 30]
unique = []

for num in numbers:
    if num not in unique:
        unique.append(num)

print(unique)

#Type_03 : Using dictionary
numbers = [10, 20, 40, 30, 50, 10, 20, 30]
unique = list(dict.fromkeys(numbers))  #dict.fromkeys() creates a dictionary with the
print(unique)
