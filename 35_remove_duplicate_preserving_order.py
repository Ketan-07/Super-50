# Remove duplicate characters while preserving order

s = "programming"

result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)