s = "aaaabbbcc"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

result = ""

for ch, count in freq.items():
    result += ch + str(count)

print(result)