# Type_01 : Using sorted()
a = "listen"
b = "silent"

if sorted(a) == sorted(b):
    print("Anagram")
else:
    print("Not Anagram")


# Type_02 : Using count() - without sorted()

a = "listen"
b = "silent"

if len(a) != len(b):
    print("Not Anagram")
else:
    is_anagram = True

    for ch in a:
        if a.count(ch) != b.count(ch):
            is_anagram = False
            break

    if is_anagram:
        print("Anagram")
    else:
        print("Not Anagram")