string = input("Enter a string: ")

for ch in string:
    if ch not in string[:string.index(ch)]:
        print(ch, ":", string.count(ch))
