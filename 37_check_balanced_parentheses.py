# Type_01 : Simple Stack

s = "((()))"

count = 0
balanced = True

for ch in s:
    if ch == "(":
        count += 1
    elif ch == ")":
        count -= 1

    if count < 0:
        balanced = False
        break

if count != 0:
    balanced = False

print(balanced)


# Type_02 : Mixed Stack

s = "({[]})"

stack = []

for ch in s:
    if ch in "([{":
        stack.append(ch)

    elif ch in ")]}":
        if not stack:
            print("Not Balanced")
            break

        top = stack.pop()

        if (ch == ')' and top != '(') or \
           (ch == ']' and top != '[') or \
           (ch == '}' and top != '{'):
            print("Not Balanced")
            break
else:
    if not stack:
        print("Balanced")
    else:
        print("Not Balanced")