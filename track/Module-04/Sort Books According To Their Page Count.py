n = int(input())
books = []

for _ in range(n):
    book_name, page_count = input().split()
    books.append((book_name, int(page_count)))

sorted_books = sorted(books, key=lambda x: x[1])

for book_name, page_count in sorted_books:
    print(book_name, page_count)