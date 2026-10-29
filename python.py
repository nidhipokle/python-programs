# Python Program to Demonstrate 7 Data Types

# 1. Numeric
num = 100
print(f"Numeric = {num}")
print("Immutable\n")

# 2. String
name = "Nidhi"
print("String = {}".format(name))
print("Immutable\n")

# 3. List
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(f"List = {fruits}")
print("Mutable\n")

# 4. Tuple
colors = ("Red", "Blue")
print("Tuple = {}".format(colors))
print("Immutable\n")

# 5. Set
numbers = {10, 20}
numbers.add(30)
print(f"Set = {numbers}")
print("Mutable\n")

# 6. Dictionary
student = {"Name": "Nidhi", "Age": 20}
student["Age"] = 21
print("Dictionary = {}".format(student))
print("Mutable\n")

# 7. Boolean
result = True
print(f"Boolean = {result}")
print("Immutable\n")

print("Summary")
print("Numeric    - Immutable")
print("String     - Immutable")
print("List       - Mutable")
print("Tuple      - Immutable")
print("Set        - Mutable")
print("Dictionary - Mutable")
print("Boolean    - Immutable")