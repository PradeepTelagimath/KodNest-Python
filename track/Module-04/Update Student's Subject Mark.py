name = input().strip()
python_mark, sql_mark, java_mark = map(int, input().split())
subject = input().strip()
new_mark = int(input())

student = {
    "name": name,
    "marks": {
        "Python": python_mark,
        "SQL": sql_mark,
        "Java": java_mark
    }
}

# Update the mark for the specified subject
student["marks"][subject] = new_mark

# Print the complete student dictionary
print(student)