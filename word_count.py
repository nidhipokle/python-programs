sentence = input("Enter a sentence: ")

count = 0
word = ""

for ch in sentence:
    if ch != " ":
        word = word + ch
    else:
        if word != "":
            count += 1
            word = ""

if word != "":
    count += 1

print("Total number of words:", count)
