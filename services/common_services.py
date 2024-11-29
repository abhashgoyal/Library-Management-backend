def view_books(book_collection):
    books = book_collection.find()
    all_books = []
    for book in books:
        all_books.append({
            "book_id": str(book["_id"]),
            "title": book["title"],
            "author": book["author"],
            "rent_price": book["rent_price"],
            "sale_price": book["sale_price"],
            "quantity": book["quantity"]
        })
    return {"response": all_books}