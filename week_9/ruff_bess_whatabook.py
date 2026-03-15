# ============================================
# Title: theBookBytes-whatABook.py
# Author: Amanda Ruff & Jarren Bess
# Course: WEB 335 – Introduction to NoSQL
# Date: 07 March 2026
# Description: Final Python application for the WhatABook project.
# ============================================

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["whatABook"]

books = db["books"]
customers = db["customers"]
wishlist = db["wishlistitems"]

# Welcome message
print("=================================")
print("       Welcome to WhatABook      ")
print("=================================")


def show_books():
    print("\nAvailable Books")
    print("-----------------------------------------------")

    for book in books.find():
        print(f"ID: {book['bookId']}")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Genre: {book['genre']}")
        print("-----------------------------------------------")


def show_books_by_genre():
    genre = input("Enter genre: ")

    print("\nBooks in Genre")
    print("-----------------------------------------------")

    for book in books.find({"genre": genre}):
        print(book["title"])


def show_books_by_author():
    author = input("Enter author: ")

    print("\nBooks by Author")
    print("-----------------------------------------------")

    for book in books.find({"author": author}):
        print(book["title"])


def show_book_by_id():
    book_id = input("Enter Book ID: ")
    book = books.find_one({"bookId": book_id})

    if book:
        print("\nBook Found")
        print("-----------------------------------------------")
        print(f"Title: {book['title']}")
        print(f"Author: {book['author']}")
        print(f"Genre: {book['genre']}")
    else:
        print("Book not found")


def view_wishlist(customer_id):
    pipeline = [
        {"$match": {"customerId": customer_id}},
        {"$lookup": {
            "from": "books",
            "localField": "bookId",
            "foreignField": "bookId",
            "as": "book"
        }}
    ]

    print("\nYour Wishlist")
    print("-----------------------------------------------")

    for item in wishlist.aggregate(pipeline):
        book = item["book"][0]
        print(book["title"])


def add_to_wishlist(customer_id):
    book_id = input("Enter Book ID to add: ")

    wishlist.insert_one({
        "customerId": customer_id,
        "bookId": book_id
    })

    print("Book added to wishlist.")


def remove_from_wishlist(customer_id):
    book_id = input("Enter Book ID to remove: ")

    wishlist.delete_one({
        "customerId": customer_id,
        "bookId": book_id
    })

    print("Book removed from wishlist.")


# Customer login
customer_id = input("Enter your customer ID: ")

customer = customers.find_one({"customerId": customer_id})

if not customer:
    print("Customer not found.")
    exit()


while True:
    print("\n========== WhatABook Menu ==========")
    print("""
1 View Books
2 View Books by Genre
3 View Books by Author
4 Search by Book ID
5 View Wishlist
6 Add Book to Wishlist
7 Remove Book from Wishlist
8 Exit
""")

    choice = input("Select option: ")

    if choice == "1":
        show_books()
    elif choice == "2":
        show_books_by_genre()
    elif choice == "3":
        show_books_by_author()
    elif choice == "4":
        show_book_by_id()
    elif choice == "5":
        view_wishlist(customer_id)
    elif choice == "6":
        add_to_wishlist(customer_id)
    elif choice == "7":
        remove_from_wishlist(customer_id)
    elif choice == "8":
        print("\nThank you for using WhatABook. Goodbye!\n")
        break