book = Book.objects.get(title='1984')
book.title = 'Nineteen Eighty-Four'
book.save()
updated_book = Book.objects.get(author='George Orwell')
print(updated_book.title)
# Expected Output: Nineteen Eighty-Four