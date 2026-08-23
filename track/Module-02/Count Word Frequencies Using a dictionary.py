n = int(input())
registrations = set()

for _ in range(n):
    student_id = input().strip()
    registrations.add(student_id)

# Read the student ID to search
search_id = input().strip()

# TODO: Calculate the number of unique registrations
unique_count = len(registrations)

# TODO: Calculate the number of duplicate entries
duplicate_count = n - unique_count

# Print the counts
print(f"Unique registrations: {unique_count}")
print(f"Duplicate entries: {duplicate_count}")

# TODO: Check whether search_id exists in registrations
if search_id in registrations:
    print("Registered")
else:
    print("Not Registered")