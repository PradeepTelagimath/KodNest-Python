n = int(input())
words = input().split()

sorted_words = sorted(words, key=len)

print(*sorted_words)