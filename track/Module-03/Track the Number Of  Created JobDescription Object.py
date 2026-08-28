class JobDescription:
    # Class-level job counter initialized to 0
    job_count = 0

    def __init__(self, role, company):
        # Store the job information as instance variables
        self.role = role
        self.company = company
        # Increase the shared counter
        JobDescription.job_count += 1


n = int(input())
jobs = []

# Read n job records and create n objects
for _ in range(n):
    role = input().strip()
    company = input().strip()
    job = JobDescription(role, company)
    jobs.append(job)

# Print the total number of created jobs
print(f"Jobs Created: {JobDescription.job_count}")