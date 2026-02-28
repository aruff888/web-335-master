"""
Title: ruff_usersp2.py
Author: Amanda Ruff
Date: 28 February 2026
Description: Exercise 7.3 - Python with MongoDB, Part II
"""

# Import MongoClient
from pymongo import MongoClient
import datetime

# Build a connection string to connect to MongoDB
client = MongoClient(
    "mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority"
)

# Configure variable to access web335DB
db = client['web335DB']

print("\n-- INSERTING DOCUMENT --")

# Step 3: Create a new user document
new_user = {
    "firstName": "Amanda",
    "lastName": "Ruff",
    "employeeId": "1014",
    "email": "aruff@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert document into users collection
new_user_id = db.users.insert_one(new_user).inserted_id
print("Inserted user id:", new_user_id)

# Step 4: Prove the document was created
print("\n-- DISPLAYING INSERTED DOCUMENT --")
print(db.users.find_one({"employeeId": "1014"}))


print("\n-- UPDATING DOCUMENT --")

# Step 5: Update the email address
db.users.update_one(
    {"employeeId": "1014"},
    {
        "$set": {
            "email": "amanda.ruff@me.com"
        }
    }
)

# Step 6: Prove the document was updated
print("\n-- DISPLAYING UPDATED DOCUMENT --")
print(db.users.find_one({"employeeId": "1014"}))


print("\n-- DELETING DOCUMENT --")

# Step 7: Delete the document
delete_result = db.users.delete_one({"employeeId": "1014"})
print("Deleted count:", delete_result.deleted_count)

# Step 8: Prove the document was deleted
print("\n-- PROVING DOCUMENT DELETION --")
print(db.users.find_one({"employeeId": "1014"}))