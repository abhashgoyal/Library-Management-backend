# from fastapi import FastAPI, Depends
# from db.connect_db import connect_db
# from modals.users import Role, User
# from modals.books import BookRent, BookBought
# from utils.authentication import require_role, get_current_user
# from utils.signup import signup
# from utils.login import login
# from modals.books import Book
# from services.admin_services import (
#     add_book, 
#     view_rented_books, 
#     view_all_users_or_moderators, 
#     delete_user, 
#     delete_moderator, 
#     delete_book
# )
# from services.moderator_services import (
#     give_book_on_rent,
#     update_book_return
# )
# from services.user_services import (
#     buy_book,
#     view_purchased_books,
#     get_book
# )
# from services.common_services import view_books
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],  # Replace with the actual origin(s)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all HTTP methods
#     allow_headers=["*"],  # Allow all headers
# )

# user_client = None
# book_client = None
# book_rent_client = None
# book_bought_client = None
# @app.on_event("startup")
# async def startup_event():
#     global user_client, book_client, book_rent_client, book_bought_client
#     user_client, book_client, book_rent_client, book_bought_client = connect_db()


# @app.on_event("shutdown")
# async def shutdown_event():
#     if user_client:
#         await user_client.close()
#     if book_client:
#         await book_client.close()
#     if book_rent_client:
#         await book_rent_client.close()
#     if book_bought_client:
#         await book_bought_client.close()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# # public routes
# @app.get("/get-books/{book_id}")
# def get_Book(book_id: str):
#     return get_book(book_client, book_id)

# @app.post("/signup")
# def signUp(user: User):
#     return signup(user_client, user.model_dump())

# @app.post("/login")
# def logIn(user: User):
#     return login(user_client, user.model_dump())


# # admin routes
# @app.post("/admin/add-book")
# def add_Book(book: Book, user: User = Depends(require_role([Role.ADMIN]))):
#     return add_book(book_collection=book_client, book=book.model_dump())

# @app.get("/admin/view-rented-books")
# def view_Rented_Books(user: User = Depends(require_role([Role.ADMIN, Role.MODERATOR]))):
#     return view_rented_books(book_rent_client)


# @app.get("/admin/view-all-users")
# def view_All_Users(user: User = Depends(require_role([Role.ADMIN]))):
#     return view_all_users_or_moderators(user_client, "user")



# @app.get("/admin/view-all-moderators")
# def view_All_Moderators(user: User = Depends(require_role([Role.ADMIN]))):
#     return view_all_users_or_moderators(user_client, "moderator")


# @app.delete("/admin/delete-user/{user_id}")
# def delete_User(user_id: str, user: User = Depends(require_role([Role.ADMIN]))):
#     return delete_user(user_client, user_id)


# @app.delete("/admin/delete-moderator/{user_id}")
# def delete_Moderator(user_id: str, user: User = Depends(require_role([Role.ADMIN]))):
#     return delete_moderator(user_client, user_id)

# @app.delete("/admin/delete-book/{book_id}")
# def delete_Book(book_id: str, user: User = Depends(require_role([Role.ADMIN]))):
#     return delete_book(book_client, book_id)



# # moderator routes
# @app.post("/moderator/give-book-on-rent")
# def give_Book_On_Rent(book_rent: BookRent, user: User = Depends(require_role([Role.MODERATOR]))):
#     return give_book_on_rent(book_rent_client, book_rent.model_dump())


# @app.put("/moderator/update-book-return")
# def update_Book_Return(book_rent: BookRent, user: User = Depends(require_role([Role.MODERATOR]))):
#     return update_book_return(book_rent_client, book_rent.model_dump())

# # user routes

# @app.post("/user/buy-book")
# def buy_Book(book_bought: BookBought, user: User = Depends(require_role([Role.USER]))):
#     return buy_book(book_bought_client, book_bought.model_dump())


# @app.get("/user/view-purchased-books/{user_id}")
# def view_Purchased_Books(user_id: str, user: User = Depends(require_role([Role.USER]))):
#     return view_purchased_books(book_bought_collection=book_bought_client, user_id=user_id)

# # common routes
# @app.get("/api/view-books")
# def view_Books(user: User = Depends(require_role([Role.USER, Role.MODERATOR, Role.ADMIN]))):
#     return view_books(book_client)

# @app.post("/logout")
# def logout(user: User = Depends(get_current_user)):
#     # Implement logout logic here (e.g., invalidate token)
#     return {"message": "Successfully logged out"}

from fastapi import FastAPI, Depends
from db.connect_db import connect_db
from modals.users import Role, User
from modals.books import BookRent, BookBought
from utils.authentication import require_role, get_current_user
from utils.signup import signup
from utils.login import login
from modals.books import Book
from services.admin_services import (
    add_book,
    view_rented_books,
    view_all_users_or_moderators,
    delete_user,
    delete_moderator,
    delete_book,
    add_user,
    add_moderator,
)
from services.moderator_services import (
    give_book_on_rent,
    update_book_return,
)
from services.user_services import (
    buy_book,
    view_purchased_books,
    get_book,
)
from services.common_services import view_books
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Replace with the actual origin(s)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

user_client = None
book_client = None
book_rent_client = None
book_bought_client = None


@app.on_event("startup")
async def startup_event():
    global user_client, book_client, book_rent_client, book_bought_client
    user_client, book_client, book_rent_client, book_bought_client = connect_db()


@app.on_event("shutdown")
async def shutdown_event():
    if user_client:
        await user_client.close()
    if book_client:
        await book_client.close()
    if book_rent_client:
        await book_rent_client.close()
    if book_bought_client:
        await book_bought_client.close()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# public routes
@app.get("/get-books/{book_id}")
def get_Book(book_id: str):
    return get_book(book_client, book_id)


@app.post("/signup")
def signUp(user: User):
    return signup(user_client, user.model_dump())


@app.post("/login")
def logIn(user: User):
    return login(user_client, user.model_dump())


# admin routes
@app.post("/admin/add-book")
def add_Book(book: Book, user: User = Depends(require_role([Role.ADMIN]))):
    return add_book(book_collection=book_client, book=book.model_dump())


@app.get("/admin/view-rented-books")
def view_Rented_Books(user: User = Depends(require_role([Role.ADMIN, Role.MODERATOR]))):
    return view_rented_books(book_rent_client)


@app.get("/admin/view-all-users")
def view_All_Users(user: User = Depends(require_role([Role.ADMIN]))):
    return view_all_users_or_moderators(user_client, "user")


@app.get("/admin/view-all-moderators")
def view_All_Moderators(user: User = Depends(require_role([Role.ADMIN]))):
    return view_all_users_or_moderators(user_client, "moderator")


@app.delete("/admin/delete-user/{user_id}")
def delete_User(user_id: str, user: User = Depends(require_role([Role.ADMIN]))):
    return delete_user(user_client, user_id)


@app.delete("/admin/delete-moderator/{user_id}")
def delete_Moderator(user_id: str, user: User = Depends(require_role([Role.ADMIN]))):
    return delete_moderator(user_client, user_id)


@app.delete("/admin/delete-book/{book_id}")
def delete_Book(book_id: str, user: User = Depends(require_role([Role.ADMIN]))):
    return delete_book(book_client, book_id)


# Add user and Add moderator routes
@app.post("/admin/add-user")
def add_User(user: User, user_data: User = Depends(require_role([Role.ADMIN]))):
    return add_user(user_client, user.model_dump())


@app.post("/admin/add-moderator")
def add_Moderator(user: User, user_data: User = Depends(require_role([Role.ADMIN]))):
    return add_moderator(user_client, user.model_dump())


# moderator routes
@app.post("/moderator/give-book-on-rent")
def give_Book_On_Rent(book_rent: BookRent, user: User = Depends(require_role([Role.MODERATOR]))):
    return give_book_on_rent(book_rent_client, book_rent.model_dump())


@app.put("/moderator/update-book-return")
def update_Book_Return(book_rent: BookRent, user: User = Depends(require_role([Role.MODERATOR]))):
    return update_book_return(book_rent_client, book_rent.model_dump())


# user routes
@app.post("/user/buy-book")
def buy_Book(book_bought: BookBought, user: User = Depends(require_role([Role.USER]))):
    return buy_book(book_bought_client, book_bought.model_dump())


@app.get("/user/view-purchased-books/{user_id}")
def view_Purchased_Books(user_id: str, user: User = Depends(require_role([Role.USER]))):
    return view_purchased_books(book_bought_collection=book_bought_client, user_id=user_id)


# common routes
@app.get("/api/view-books")
def view_Books(user: User = Depends(require_role([Role.USER, Role.MODERATOR, Role.ADMIN]))):
    return view_books(book_client)


@app.post("/logout")
def logout(user: User = Depends(get_current_user)):
    return {"message": "Successfully logged out"}
