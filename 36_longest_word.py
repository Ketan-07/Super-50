# Find the longest word

s = "Python is very powerful"
words = s.split()
longest = ""

for word in words:
    if len(word)>len(longest):
        longest=word

print(longest)