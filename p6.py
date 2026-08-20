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

    def has_skill(self, skill_name):
        searched_skill = skill_name.strip().lower()

        for skill in self.skills:
            if skill.strip().lower() == searched_skill:
                return True

        return False


# Read input from the user
student_id = int(input())
name = input().strip()
course = input().strip()
score = float(input())
skills_input = input().strip()
placement_input = input().strip()
skill_to_find = input().strip()

# Convert skills into a list of cleaned skill names
skills = [
    s.strip()
    for s in skills_input.split(",")
    if s.strip()
]

# Convert placement status to boolean
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

# Call has_skill() and print the required result
if student.has_skill(skill_to_find):
    print("Skill Found")
else:
    print("Skill Not Found")
