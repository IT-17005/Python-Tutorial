books = []
books.append("সি++")
books.append("জাভা")
books.append("পাইথন")
print(books)
books.pop()
print("Now the top books is:",books[-1])
books.pop()
print("Now the top books is:",books[-1])
books.pop()
if not books:
    print("No books left.")