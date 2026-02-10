/**
 * Author: Amanda Ruff
 * Date: 02/09/26
 * Assignment: Hands-On 5.1 – MongoDB Document Manipulation and Projections
 * Description: MongoDB shell queries for user collection manipulation.
 */

/**
 * Query 1:
 * Add a new user to the users collection.
 */
db.users.insertOne({
  firstName: "Ludwig",
  lastName: "Beethoven",
  email: "beethoven@music.com",
  employeeId: "1012",
  dateCreated: new Date()
});

/**
 * Query 1 Proof:
 * Verify the new user was added successfully.
 */
db.users.find({ lastName: "Beethoven" });

/**
 * Query 2:
 * Update Mozart’s email address.
 */
db.users.updateOne(
  { lastName: "Mozart" },
  { $set: { email: "mozart@me.com" } }
);

/**
 * Query 2 Proof:
 * Verify Mozart’s email was updated.
 */
db.users.find({ lastName: "Mozart" });

/**
 * Query 3:
 * Display all users using projections.
 * Show only first name, last name, and email.
 */
db.users.find(
  {},
  {
    firstName: 1,
    lastName: 1,
    email: 1,
    _id: 0
  }
);
