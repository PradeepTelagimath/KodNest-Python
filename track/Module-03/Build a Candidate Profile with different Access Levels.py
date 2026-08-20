class CandidateProfile:
    def __init__(self, name, email, score):
        self.name = name
        self._email = email
        self.__score = score

    def get_email(self):
        return self._email

    def get_score(self):
        return self.__score


# Read inputs
name = input().strip()
email = input().strip()
score = int(input().strip())

# Create one CandidateProfile object
candidate = CandidateProfile(name, email, score)

# Output candidate profile
print("CANDIDATE PROFILE")
print(f"Name: {candidate.name}")
print(f"Email: {candidate.get_email()}")
print(f"Score: {candidate.get_score()}")