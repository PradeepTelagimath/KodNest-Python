sentence = input()

#clean and normalize the sentence
clean = sentence.strip()
normalize = clean.lower().replace(".", " ")

# Split the sentence and create the slug
words = normalize.split()
slug = "-".join(words)

# Produce the uppercase from and search result 
uppercase = normalize.upper()
python_position = normalize.find("python")

#Display all processed values
print(f"Cleaned: {clean}")
print(f"Normalized: {normalize}")
print(f"Words: {words}")
print(f"Slug: {slug}")
print(f"Uppercase: {uppercase}")
print(f"Python position: {python_position}")   