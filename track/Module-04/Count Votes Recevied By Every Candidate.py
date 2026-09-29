from collections import Counter

votes = input().split()

vote_counts = Counter(votes)

for candidate, count in vote_counts.items():
    print(f"{candidate}: {count}")
    