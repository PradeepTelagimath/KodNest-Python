from collections import Counter

skills = input().split()

counter = Counter(skills)
most_common_skill, count = counter.most_common(1)[0]

print(f"{most_common_skill}: {count}")