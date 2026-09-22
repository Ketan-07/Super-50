# Non-repeating characters
s="abfjdfbvxjhdbhvjeygfkeabjhk"
a=""
for i in s:
    if s.count(i)==1:
        a+=i

print(a)


# Find first non-repeating character
s = "aabbcdde"

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break