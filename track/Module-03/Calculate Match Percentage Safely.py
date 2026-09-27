def calculate_match_percentage(required_skills, matching_skills):
    # Handle division by zero case when required_skills is 0
    if required_skills == 0:
        return 0
    
    # Calculate match percentage
    match_percentage = (matching_skills / required_skills) * 100
    return match_percentage

required_skills = int(input())
matching_skills = int(input())
print(calculate_match_percentage(required_skills, matching_skills))