numbers = [10, 15, 22, 31, 44, 57, 68, 73, 80, 91, 12, 25, 36, 49, 50]

even_count = 0
odd_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print("List of integers:")
print(numbers)

print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
