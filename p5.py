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
        self.student_id = student_id
        self.name = name
        self.course = course
        self.score = score
        self.skills = skills
        self.is_placed = is_placed

    def __str__(self):
        skills_text = ", ".join(self.skills)
        placement_status = (
            "Placed" if self.is_placed
            else "Not Placed"
        )

        return f"""Student ID: {self.student_id}
Name: {self.name}
Course: {self.course}
Score: {self.score:.1f}
Skills: {skills_text}
Placement Status: {placement_status}"""


student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()

skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

is_placed = placement_input.lower() == "yes"

student = StudentProfile(
    student_id,
    name,
    course,
    score,
    skills,
    is_placed
)

print(student)
