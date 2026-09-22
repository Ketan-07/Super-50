n = int(input("Enter a num"))
rev = 0
while n > 0:
    temp = n % 10
    rev = rev * 10 + temp
    n = n//10

print(f"Reverse of the number is {rev}")