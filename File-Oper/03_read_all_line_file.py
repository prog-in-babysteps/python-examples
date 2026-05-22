# Reading a file line by line in loop
with open('data\\books.txt', 'r') as book_file:
    all_lines = book_file.readlines()
    print("File Content:")
    print(all_lines)
