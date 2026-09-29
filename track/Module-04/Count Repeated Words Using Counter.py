from collections import Counter

words = input().split()

counts = Counter(words)

for word, count in counts.items():
    print(f"{word}: {count}")