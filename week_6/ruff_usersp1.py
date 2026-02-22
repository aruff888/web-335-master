"""
Title: ruff_usersp1.py
Author: Amanda Ruff
Date: 22 February 2026
Description: Hands-On 4.2 – Python with MongoDB, Part I
"""

# Import MongoClient
from pymongo import MongoClient

# Build the connection string
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority"
)

# Access the web335DB database
db = client["web335DB"]

print("\n-- DISPLAYING ALL USERS --")
for user in db.users.find():
    print(user)

print("\n-- DISPLAYING USER WITH employeeId 1011 --")
print(db.users.find_one({"employeeId": "1011"}))

print("\n-- DISPLAYING USER WITH lastName Mozart --")
print(db.users.find_one({"lastName": "Mozart"}))