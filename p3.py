class StudentProfile:
    def __init__(self, student_id, name, course):
        # Store the received values in instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course


student_id = int(input())
name = input().strip()
course = input().strip()

# Create a StudentProfile object
student = StudentProfile(student_id, name, course)

# Print the stored student details
print(f"Student ID: {student.student_id}")
print(f"Name: {student.name}")
print(f"Course: {student.course}")
