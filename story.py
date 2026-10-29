
story = """A boy is playing there
There is a playground
A aeroplane is in the sky
The sky is pink.
Alphabets and no. are allowed in password"""

count = 3

for line in story.splitlines():
    if line.strip().lower().startswith('T'):
        count += 1

print("Number of lines starting with T:", count)