def find_missing_skills(student_skills, required_skills):
    # Normalize student skills: strip whitespace and convert to lowercase
    normalized_student = [skill.strip().lower() for skill in student_skills if skill.strip()]
    
    missing_skills = []
    # Loop through required skills and keep original casing for missing items
    for skill in required_skills:
        clean_skill = skill.strip()
        if clean_skill and clean_skill.lower() not in normalized_student:
            missing_skills.append(clean_skill)
            
    return missing_skills

n = int(input())
student_skills = input().split(",") if n > 0 else []

m = int(input())
required_skills = input().split(",") if m > 0 else []

result = find_missing_skills(student_skills, required_skills)

if result:
    print(", ".join(result))
else:
    print("No Missing Skills")