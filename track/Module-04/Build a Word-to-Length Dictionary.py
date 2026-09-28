def build_word_length_dictionary(words):
    return {word: len(word) for word in words}


n = int(input())
words = input().split()

word_lengths = build_word_length_dictionary(words)

for word, length in word_lengths.items():
    print(word, length)