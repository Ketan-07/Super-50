numbers = [2, 2, 1, 1, 1, 2, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

for num in frequency:
    if frequency[num] > len(numbers) // 2:
        print("Majority element:", num)
        break