# Application Form using File Handling

while True:

    name = input("Enter Name: ")
    mobile = input("Enter Mobile Number: ")
    email = input("Enter Email: ")

    file = open("application.txt", "a")

    file.write("Name: " + name + "\n")
    file.write("Mobile Number: " + mobile + "\n")
    file.write("Email: " + email + "\n")

    file.close()

    print("Data saved successfully.")

    choice = input("Do you want to enter another user? (yes/no): ")

    if choice.lower() == "no":
        break

file = open("application.txt", "r")

print(file.read())
file.close()

