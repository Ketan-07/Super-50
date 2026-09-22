# Find pairs with given sum

# Type_01 : Using two for loop 
numbers = [2, 7, 11, 15]
target = 9

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] ==  target:
            print(numbers[i],numbers[j])

# Type_02 : Using Single for loop and slicing
numbers = [2, 7, 11, 15]
target = 18

for i in range(len(numbers)):
    complement = target - numbers[i]
    if complement in numbers[i+1:]:
        print(numbers[i],complement)
        break