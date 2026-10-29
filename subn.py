
import re

text = "cat and cat"

result = re.subn("cat", "dog", text)

print(result)
