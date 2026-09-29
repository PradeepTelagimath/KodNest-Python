from collections import Counter

issues = input().split()

counter = Counter(issues)
top_two = counter.most_common(2)

for issue, count in top_two:
    print(f"{issue}: {count}")