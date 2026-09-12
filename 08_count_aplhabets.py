# Type_01: Using isinstance() and isalpha()
items = ['a', 'b', 10, 'c', 20, 'd']

count = 0

for item in items:
    if isinstance(item, str) and item.isalpha():
        count += 1

print(count)

# Type_02: Using type() and isalpha()
items = ['a', 'b', 10, 'c', 20, 'd']

count = 0

for item in items:
    if type(item) == str and item.isalpha():
        count += 1

print(count)

#Type_03: Using try-except block
items = ['a', 'b', 10, 'c', 20, 'd']

count = 0

for item in items:
    try:
        if item.isalpha():
            count += 1
    except AttributeError:
        pass

print(count)