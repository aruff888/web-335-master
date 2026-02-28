
// BookBytes-WhatABook.js
// MongoDB Queries for WhatABook Project
// Author: Amanda Ruff and Jarren Bess

// 1. Display all books
db.books.find({})

// 2. Display books by genre
db.books.find({ genre: "Fiction" })

// 3. Display books by author
db.books.find({ author: "Harper Lee" })

// 4. Display book by bookId
db.books.findOne({ bookId: "b1007" })

// 5. Display wishlist by customerId using $lookup
db.wishlistitems.aggregate([
  { $match: { customerId: "c1007" } },
  {
    $lookup: {
      from: "books",
      localField: "bookId",
      foreignField: "bookId",
      as: "bookDetails"
    }
  }
])

// 6. Add book to wishlist
db.wishlistitems.insertOne({
  customerId: "c1007",
  bookId: "b1008"
})

// 7. Remove book from wishlist
db.wishlistitems.deleteOne({
  customerId: "c1007",
  bookId: "b1008"
})
