s = input()
moji = ["dream", "dreamer", 'erase', 'eraser']
while s != "":
    if s[-5:] == moji[0]:
        s = s[:-5]
    elif s[-7:] == moji[1]:
        s = s[:-7]
    elif s[-5:] == moji[2]:
        s = s[:-5]
    elif s[-6:] == moji[3]:
        s = s[:-6]
    else:
        break
if s == "":
    print("YES")
else:
    print("NO")
