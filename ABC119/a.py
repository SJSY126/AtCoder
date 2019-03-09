s = input()
s = s[:4]+s[5:7]+s[8:]

if int(s) <= 20190430:
    print("Heisei")
else:
    print("TBD")
