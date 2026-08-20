class StudentProfile:
    def __init__(
        self,
        student_id,
        name,
        course,
        score,
        skills,
        is_placed
    ):
        # Store all received values in instance attributes
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed


# Read input from the user
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()

# Convert skills into a list of skill names
skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

# Convert placement input into a Boolean value
is_placed = placement_input.lower() == "yes"

# Create exactly one StudentProfile object
student = StudentProfile(
    student_id,
    name,
    course,
    score,
    skills,
    is_placed
)

# Format outputs for printing
skills_text = ", ".join(student.skills)
placement_status = (
    "Placed" if student.is_placed
    else "Not Placed"
)

# Print the stored student details
print(f"Student ID: {student.student_id}")
print(f"Name: {student.name}")
print(f"Course: {student.course}")
print(f"Score: {student.score:.1f}")
print(f"Skills: {skills_text}")
print(f"Placement Status: {placement_status}")
