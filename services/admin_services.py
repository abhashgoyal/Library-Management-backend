# from bson.objectid import ObjectId

# def add_book(book_collection, book: dict):
#     book_collection.insert_one(book)
#     return {"status": 200, "message": "Book added successfully"}

# # can also view books which are given as rent
# def view_rented_books(book_rent_collection):
#     rent_books = book_rent_collection.find()
#     all_rent_books = []
#     for rent_book in rent_books:
#         all_rent_books.append({
#             "_id": str(rent_book["_id"]),
#             "book_id": rent_book["book_id"],
#             "user_id": rent_book["user_id"],
#             "rent_price": rent_book["rent_price"],
#             "issue_date": rent_book["issue_date"],
#             "return_date": rent_book["return_date"],
#             "is_returned": rent_book["is_returned"]
#         })
#     return {"response": all_rent_books}


# def view_all_users_or_moderators(user_collection, role: str):
#     users = user_collection.find()
#     all_users = []
#     for user in users:
#         all_users.append({
#             "user_id": str(user["_id"]),  # Convert ObjectId to string
#             "username": user["username"],
#             "email": user["email"], 
#             "role": user["role"]
#         })

#     all_users = [users for users in all_users if users["role"] == role]
#     return {"response": all_users}


# def delete_user(user_collection, user_id: str):
#     user_collection.delete_one({"_id": ObjectId(user_id)})
#     return {"status": 200, "message": "User deleted successfully"}


# def delete_moderator(user_collection, user_id: str):
#     user_collection.delete_one({"_id": ObjectId(user_id)})
#     return {"status": 200, "message": "Moderator deleted successfully"}


# def delete_book(book_collection, book_id: str):
#     book_collection.delete_one({"_id": ObjectId(book_id)})
#     return {"status": 200, "message": "Book deleted successfully"}

from modals.users import User
from bson.objectid import ObjectId

# Add User
def add_user(user_collection, user: dict):
    try:
        existing_user = user_collection.find_one({"email": user["email"]})
        if existing_user:
            return {"status": 400, "message": "User with this email already exists"}

        user_collection.insert_one(user)
        return {"status": 200, "message": "User added successfully"}
    except Exception as e:
        return {"status": 500, "message": str(e)}

# Add Moderator
def add_moderator(user_collection, user: dict):
    try:
        existing_moderator = user_collection.find_one({"email": user["email"]})
        if existing_moderator:
            return {"status": 400, "message": "Moderator with this email already exists"}

        # Assign the role to moderator
        user["role"] = "moderator"
        user_collection.insert_one(user)
        return {"status": 200, "message": "Moderator added successfully"}
    except Exception as e:
        return {"status": 500, "message": str(e)}

# Delete User
def delete_user(user_collection, user_id: str):
    user_collection.delete_one({"_id": ObjectId(user_id)})
    return {"status": 200, "message": "User deleted successfully"}

# Delete Moderator
def delete_moderator(user_collection, user_id: str):
    user_collection.delete_one({"_id": ObjectId(user_id)})
    return {"status": 200, "message": "Moderator deleted successfully"}

# Delete Book
def delete_book(book_collection, book_id: str):
    book_collection.delete_one({"_id": ObjectId(book_id)})
    return {"status": 200, "message": "Book deleted successfully"}

# Add Book
def add_book(book_collection, book: dict):
    book_collection.insert_one(book)
    return {"status": 200, "message": "Book added successfully"}

# View Rented Books
def view_rented_books(book_rent_collection):
    rent_books = book_rent_collection.find()
    all_rent_books = []
    for rent_book in rent_books:
        all_rent_books.append({
            "_id": str(rent_book["_id"]),
            "book_id": rent_book["book_id"],
            "user_id": rent_book["user_id"],
            "rent_price": rent_book["rent_price"],
            "issue_date": rent_book["issue_date"],
            "return_date": rent_book["return_date"],
            "is_returned": rent_book["is_returned"]
        })
    return {"response": all_rent_books}

# View Users or Moderators
def view_all_users_or_moderators(user_collection, role: str):
    users = user_collection.find()
    all_users = []
    for user in users:
        all_users.append({
            "user_id": str(user["_id"]),  # Convert ObjectId to string
            "username": user["username"],
            "email": user["email"], 
            "role": user["role"]
        })

    all_users = [users for users in all_users if users["role"] == role]
    return {"response": all_users}
