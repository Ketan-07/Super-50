# Implement your own map()

def my_map(func, items):
    result = []

    for item in items:
        result.append(func(item))

    return result


numbers = [1, 2, 3]

print(my_map(lambda x: x * 2, numbers))