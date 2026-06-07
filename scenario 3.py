

# A teacher has a list of student names and a dictionary
#that stores their marks in a result sheet.
# Write a Python program to display each student's marks,
#calculate the class average, and determine the highest and lowest marks.
# List of students
students = ["Ali", "Sara", "Ayesha", "Hamza", "Usman"]

# Dictionary of marks
marks = {
    "Ali": 85,
    "Sara": 92,
    "Ayesha": 78,
    "Hamza": 88,
    "Usman": 95
}

# Display marks
print("Student Marks:")
for name in students:
    print(name, ":", marks[name])

# Highest & Lowest
highest = max(marks, key=marks.get)
lowest = min(marks, key=marks.get)
print((highest,lowest))

# Class average
avg = sum(marks.values()) / len(marks)

print("\nHighest Marks:", highest, "=", marks[highest])
print("Lowest Marks:", lowest, "=", marks[lowest])
print("Class Average:", avg)
