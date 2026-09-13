# Type_01 : Using for loop

n = 10

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Type_02 : Using Recursion

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 10

for i in range(n):
    print(fibonacci(i), end=" ")