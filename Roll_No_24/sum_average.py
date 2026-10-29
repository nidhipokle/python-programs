numbers = []

print("Enter 10 numbers:")

for i in range(10):
    number = int(input("Enter number: "))
    numbers.append(number)

sum_of_numbers = 0

for number in numbers:
    sum_of_numbers = sum_of_numbers + number

average = sum_of_numbers / 10

print("List of numbers:")
print(numbers)

print("Sum:", sum_of_numbers)
print("Average:", average)
