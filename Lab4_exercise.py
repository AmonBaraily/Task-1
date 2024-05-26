book_list = ["1986", "To Kill a guy", "The End of the World"]
author_set = ["Luis Lowry", "Homer", "Mark"]
books_dict = {1: {"title": "1986" , "author" : "Luis Lowry"}, 2: {"title": "To Kill a guy", "author": "Homer"}, 3: {"title": "The End of the World", "author": "Mark"}}

search_title = input("Enter Title:")
if search_title in book_list :
    print(f"Book Avialable! Author:{books_dict[book_list.index(search_title)+1]['author']}")
else: 
    print("Book Not Avilable")

print("All Books:")
for book in book_list:
    print(book)    

remove_book = input("Enter the title of the book to be removed or skip:")
if remove_book in book_list:
    remove_author = books_dict[book_list.index(remove_book)+1]['author']
    book_list.remove(remove_book)
    author_set.remove(remove_author) 
    del books_dict[book_list.index(remove_book)+1]
    print("Book removed successfully")
    print("Books available:", book_list) 

else: 
   print("book not found")