class JobDescription:
    def __init__(
        self,
        job_id,
        company,
        role,
        location="Remote",
        minimum_score=0.0,
        required_skills=None,
        is_active=True
    ):
        self.job_id = job_id
        self.company = company
        self.role = role
        self.location = location
        self.minimum_score = minimum_score
        self.required_skills = (
            []
            if required_skills is None
            else list(required_skills)
        )
        self.is_active = is_active

    def __str__(self):
        skills_text = ", ".join(self.required_skills)
        status = "Active" if self.is_active else "Closed"

        return f"""Job ID: {self.job_id}
Company: {self.company}
Role: {self.role}
Location: {self.location}
Minimum Score: {self.minimum_score:.1f}
Required Skills: {skills_text}
Status: {status}"""


# Read input from the user
job_id = int(input())
company = input().strip()
role = input().strip()
location = input().strip()
minimum_score = float(input())
skills_input = input().strip()
status_input = input().strip()

# Convert skills input into a list of cleaned skill names
required_skills = [
    skill.strip()
    for skill in skills_input.split(",")
    if skill.strip()
]

# Convert job status to boolean
is_active = status_input.lower() == "yes"

# Create exactly one JobDescription object
job = JobDescription(
    job_id,
    company,
    role,
    location,
    minimum_score,
    required_skills,
    is_active
)

# Print the object directly
print(job)
