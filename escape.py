
import re

text = "a+b"

pattern = re.escape(text)

print(pattern)
print(bool(re.search(pattern, "a+b")))
