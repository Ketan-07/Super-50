#Type_01 : Using dictionary
s = "banana"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1

print(freq)

#Type_02 : Using count()
s = "banana"

freq = {}

for ch in s:
    freq[ch] = s.count(ch)

print(freq)

#Type_03 : Using collections.Counter
from collections import Counter

s = "banana"
freq = Counter(s)
print(freq)