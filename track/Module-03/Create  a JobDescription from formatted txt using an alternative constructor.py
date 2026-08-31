class JobDescription:
    def __init__(self, role, company, minimum_experience, required_skills):
        self.role = role
        self.company = company
        self.minimum_experience = minimum_experience
        self.required_skills = required_skills

    @classmethod
    def from_text(cls, data):
        role_str, company_str, exp_str, skills_str = data.split(";")
        
        role = role_str.strip().title()
        company = company_str.strip()
        minimum_experience = int(exp_str)
        required_skills = [skill.strip() for skill in skills_str.split(",")]
        
        return cls(role, company, minimum_experience, required_skills)


# Read input
data = input()

# Create object using alternative constructor
job = JobDescription.from_text(data)

# Print stored job information
skills_formatted = ", ".join(job.required_skills)
print(f"Role: {job.role}")
print(f"Company: {job.company}")
print(f"Minimum Experience: {job.minimum_experience} years")
print(f"Required Skills: {skills_formatted}")