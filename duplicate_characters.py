string = input("Enter a string: ")

duplicates = ""

for ch in string:
    if string.count(ch) > 1 and ch not in duplicates:
        duplicates = duplicates + ch

print("Duplicate characters:", duplicates)
