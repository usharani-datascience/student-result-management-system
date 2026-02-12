print("===== Student Result Management System =====")
print("1. Add Student")
print("2. View Students")
print("3. Exit")

choice = input("Enter your choice: ")
print("You selected:", choice)
roll = input("Enter Roll Number: ")
name = input("Enter Name: ")

m1 = int(input("Enter Marks 1: "))
m2 = int(input("Enter Marks 2: "))
m3 = int(input("Enter Marks 3: "))

total = m1 + m2 + m3
average = total / 3

print("Total Marks:", total)
print("Average:", average)
if average >= 90:
    grade = "A+"
elif average >= 75:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)
file = open("students.txt", "a")
file.write(roll + "," + name + "," + str(total) + "," + grade + "\n")
file.close()

print("Student data saved successfully!")

