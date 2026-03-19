// ===============================
// CREATE OPERATIONS
// ===============================

// Insert multiple users
db.users.insertMany([
  {
    name: "Durgesh Sonawane",
    email: "[dugguboi@gmail.com](mailto:dugguboi@gmail.com)",
    age: 23,
    city: "Mumbai",
    is_active: true,
    purchases: [],
  },
  {
    name: "Paritosh Sandhan",
    email: "[sandyparu@gmail.com](mailto:sandyparu@gmail.com)",
    age: 22,
    city: "Nagpur",
    is_active: false,
    purchases: [],
  },
]);

// ===============================
// READ OPERATIONS
// ===============================

// Get all users
db.users.find();

// Find users from Pune
db.users.find({ city: "Pune" });

// Find users with age greater than 21
db.users.find({ age: { $gt: 21 } });

// Find active users
db.users.find({ is_active: true });

// Project only name and city
db.users.find({}, { name: 1, city: 1, _id: 0 });

// ===============================
// UPDATE OPERATIONS
// ===============================

// Update single document
db.users.updateOne({ name: "Durgesh Sonawane" }, { $set: { city: "Thane" } });

// Update multiple documents
db.users.updateMany({ city: "Pune" }, { $set: { is_active: false } });

// Add new purchase to a user
db.users.updateOne(
  { name: "Himanshu Jadhav" },
  {
    $push: {
      purchases: {
        product: "Keyboard",
        category: "Accessories",
        amount: 1500,
        date: new Date(),
      },
    },
  },
);

// ===============================
// DELETE OPERATIONS
// ===============================

// Delete one user
db.users.deleteOne({ name: "Paritosh Sandhan" });

// Delete inactive users
db.users.deleteMany({ is_active: false });
