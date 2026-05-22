# Reading a file line by line in loop
book_isbn = {}
with open('data\\books.txt', 'r') as book_file:
    for book_rec in book_file:
        book_rec = book_rec.strip()
        name, isbn, price, author, num_pages = book_rec.split(",")
        print(f"Book Name: {name} ISBN: {isbn}")


with open('data\\isbn.txt', 'w') as authors_file:
    for book_name, isbn in book_isbn.items():
        authors_file.write(f"Author Name: {author}\n")
