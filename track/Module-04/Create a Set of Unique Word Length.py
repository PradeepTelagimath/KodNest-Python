def create_unique_lengths(words):
    return {len(word) for word in words}


n = int(input())
words = input().split()

unique_lengths = create_unique_lengths(words)

ordered_lengths = [
    length
    for length in range(1, 21)
    if length in unique_lengths
]

print(*ordered_lengths)