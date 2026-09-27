def count_matches(student_skills, required_skills):
    # Normalize student skills: strip extra whitespaces and convert to lowercase
    normalized_student_skills = [skill.strip().lower() for skill in student_skills]
    
    # Normalize required skills
    normalized_required_skills = [skill.strip().lower() for skill in required_skills]
    
    count = 0
    # Check how many required skills are present in the student's normalized skill list
    for skill in normalized_required_skills:
        if skill in normalized_student_skills:
            count += 1
            
    return count

student_skills = input().split(",")
required_skills = input().split(",")
print(count_matches(student_skills, required_skills))