# 38. Find common prefix

# Type_01 : Prefix + startswith()

words = ["flower", "flow", "flight"]

prefix = words[0]

for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print(prefix)

# Type_02 : Character-by-character comparison

words = ["apple", "application", "apply"]


prefix = ""

for i in range(len(words[0])):
    ch = words[0][i]

    for word in words[1:]:
        if i >= len(word) or word[i] != ch:
            print(prefix)
            break
    else:
        prefix += ch
        continue

    break

print(prefix)