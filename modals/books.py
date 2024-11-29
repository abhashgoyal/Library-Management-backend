from pydantic import BaseModel
from typing import Optional


class Book(BaseModel):
    title: str
    author: str
    description: str
    rent_price: float
    sale_price: float
    quantity: int


class BookRent(BaseModel):
    book_id: str
    user_id: str
    rent_price: float
    issue_date: str
    return_date: str
    is_returned: bool


class BookBought(BaseModel):
    book_id: str
    user_id: str
    buy_date: str
