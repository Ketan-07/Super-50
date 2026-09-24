# Linear Search

numbers = [10, 25, 30, 45, 50]
target = 45

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        break
else:
    print("Not Found")