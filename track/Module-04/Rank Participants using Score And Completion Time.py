n = int(input())
participants = []

for _ in range(n):
    name, score, completion_time = input().split()
    participants.append((name, int(score), int(completion_time)))

# Sort participants:
# 1. Higher score first -> -x[1] (descending order)
# 2. Lower completion time first -> x[2] (ascending order)
participants.sort(key=lambda x: (-x[1], x[2]))

# Print the ranked participants
for name, score, completion_time in participants:
    print(f"{name} {score} {completion_time}")