/**
============================================
; Title: whatabook_queries.js
; Author: Amanda Ruff & Jarren Bess
; Date: 03 March 2026
; Description: Query demonstrations for the WhatABook database
;===========================================
*/

// Switch to whatABook database
use whatABook;

// ==============================
// Display all books
// ==============================

db.books.find().pretty();

// ==============================
// Display books by genre
// ==============================

db.books.find({ genre: "Fiction" }).pretty();

// ==============================
// Display books by author
// ==============================

db.books.find({ author: "Harper Lee" }).pretty();

// ==============================
// Display book by bookId
// ==============================

db.books.find({ bookId: "b1001" }).pretty();