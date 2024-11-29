"""
We have a library management system.
So the user will have two functionalities:
1. To buy books
2. To view books
"""
from bson.objectid import ObjectId

def buy_book(book_collection, book):
    book_collection.insert_one(book)
    return {"status": 200, "message": "Book bought successfully"}

def view_purchased_books(book_bought_collection, user_id):
    books = book_bought_collection.find({"user_id": user_id})
    books_list = []
    for book in books:
        books_list.append(book["book_id"])

    return {"status": 200, "books": books_list}


def get_book(book_collection, book_id):
    book = book_collection.find_one({"_id": ObjectId(book_id)})
    book["_id"] = str(book["_id"])
    return {"status": 200, "book": book}



