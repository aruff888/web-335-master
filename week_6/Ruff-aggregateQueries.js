/**
 * Amanda Ruff
 * Assignment 6.2 – Aggregate Queries
 * Date: 02/18/26
 */

/**
 * a. Display all students
 */
db.students.find().pretty();

/**
 * b. Add a new student
 */
db.students.insertOne({
  studentId: "1010",
  firstName: "Harry",
  lastName: "Potter",
  houseId: "G",
  age: 17
});

/**
 * Prove the student was added
 */
db.students.find({ studentId: "1010" }).pretty();

/**
 * c. Update the student’s age
 */
db.students.updateOne(
  { studentId: "1010" },
  { $set: { age: 18 } }
);

/**
 * Prove update
 */
db.students.find({ studentId: "1010" }).pretty();

/**
 * d. Delete the student
 */
db.students.deleteOne({ studentId: "1010" });

/**
 * Prove deletion
 */
db.students.find({ studentId: "1010" }).pretty();

/**
 * e. Display all students by house
 */
db.houses.aggregate([
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  }
]);

/**
 * f. Display all students in Gryffindor
 */
db.houses.aggregate([
  { $match: { name: "Gryffindor" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  }
]);

/**
 * g. Display students in the house with an Eagle mascot
 */
db.houses.aggregate([
  { $match: { mascot: "Eagle" } },
  {
    $lookup: {
      from: "students",
      localField: "houseId",
      foreignField: "houseId",
      as: "students"
    }
  }
]);
