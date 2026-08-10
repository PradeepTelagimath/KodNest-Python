skills = []

#Read and store five skills
for i in range(5):
    skill = input()
    skills.append(skill)

# convert the list into tuple 
skill_record=tuple(skills)

# Display all required results
print("Skill Record:",skill_record)
print("First Three:",skill_record[0:3])
print("Last Two:",skill_record[-2:])
print("Alternate Skills:",skill_record[::2]) 
print("Reversed SKills:",skill_record[::-1]) 
