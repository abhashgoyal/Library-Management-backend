def give_book_on_rent(book_rent_collection, book_rent):
    book_rent_collection.insert_one(book_rent)
    return {"status": 200, "message": "Book rented successfully"}


# ! yet to be done:


def update_book_return(book_rent_collection, book_rent):
    book_rent_collection.update_one({"book_id": book_rent["book_id"], "user_id": book_rent["user_id"]}, {"$set": {"is_returned": True}})
    return {"status": 200, "message": "Book returned successfully"}

