# Implement your own filter()

def my_filter(func, items):
    result = []

    for item in items:
        if func(item):
            result.append(item)

    return result


numbers = [1, 2, 3, 4, 5]

print(my_filter(lambda x: x % 2 == 0, numbers))