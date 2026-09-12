#Type_01: Using split()
s = "This is a sample sentence with several words"
words = s.split()
print(len(words))

#Type_02: Using list comprehension
s = "This is a sample sentence with several words"
words = [word for word in s.split()]
print(len(words))

#Type_03: Using re.findall()
import re
s = "This is a sample sentence with several words"
words = re.findall(r'\b\w+\b', s)
print(len(words))