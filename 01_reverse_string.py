# Reverse a string

# Type_1 : Using slicing

s = "Python"
rev = s[::-1]

print(rev)

# Type_2 : Using a loop
s = "Python"
rev = ""
for i in s:
    rev = i + rev
print(rev)

# Type_3 : Using reversed() function
s = "Python"
rev = ''.join(reversed(s))   #reversed() returns the characters of a string in reverse order as an iterator
print(rev)                   #I use join() to combine those characters and convert them back into a string