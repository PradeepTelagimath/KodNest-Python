class JobDescription:
    platform_name = "KodNest Jobs"

    def __init__(self, role, company, minimum_experience):
        self.role = role
        self.company = company
        self.minimum_experience = minimum_experience

    @staticmethod
    def is_valid_experience(experience):
        return 0 <= experience <= 20

    @classmethod
    def from_text(cls, data):
        role, company, exp_str = data.split("|")
        experience = int(exp_str)

        if not cls.is_valid_experience(experience):
            return None

        formatted_role = role.strip().title()
        formatted_company = company.strip()

        return cls(formatted_role, formatted_company, experience)


# Read input outside the class
data = input()

# Create job using from_text()
job = JobDescription.from_text(data)

if job is not None:
    print(f"Platform: {JobDescription.platform_name}")
    print(f"Role: {job.role}")
    print(f"Company: {job.company}")
    print(f"Minimum Experience: {job.minimum_experience} years")
else:
    print("Invalid Experience")