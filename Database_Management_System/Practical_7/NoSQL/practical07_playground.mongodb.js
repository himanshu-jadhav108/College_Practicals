// MongoDB Playground for Practical 07
// Objective: Demonstrate CRUD, Aggregation, and Indexing
// Maintainer: Himanshu Jadhav

// Step 1: Create and switch to the database
const database = "practical07";
const collection = "users";

use(database);

// Step 2: Create the 'users' collection
db.createCollection(collection);

// Step 3: Insert sample documents (anime characters for fun)
db.users.insertMany([
  { name: "Himanshu Jadhav", age: 21, email: "himanshu@example.com", city: "Malegaon", purchase_amount: 1200 },
  { name: "Baku Madarame", age: 25, email: "baku@example.com", city: "Tokyo", purchase_amount: 800 },
  { name: "Naruto Uzumaki", age: 30, email: "naruto@example.com", city: "Konoha", purchase_amount: 1500 },
  { name: "Ichigo Kurosaki", age: 28, email: "ichigo@example.com", city: "Karakura", purchase_amount: 600 },
  { name: "Eren Yeager", age: 22, email: "eren@example.com", city: "Shiganshina", purchase_amount: 950 },
  { name: "Levi Ackerman", age: 35, email: "levi@example.com", city: "Shiganshina", purchase_amount: 2000 },
  { name: "Sasuke Uchiha", age: 27, email: "sasuke@example.com", city: "Konoha", purchase_amount: 1800 },
  { name: "Light Yagami", age: 24, email: "light@example.com", city: "Tokyo", purchase_amount: 2200 }
]);

// Step 4: CRUD Operations
// Read all documents
db.users.find();

// Update Eren's city
db.users.updateOne({ name: "Eren Yeager" }, { $set: { city: "Paradise Island" } });

// Delete Ichigo
db.users.deleteOne({ name: "Ichigo Kurosaki" });

// Step 5: Aggregation Examples
// Average age of users
db.users.aggregate([{ $group: { _id: null, avgAge: { $avg: "$age" } } }]);

// Total purchase amount
db.users.aggregate([{ $group: { _id: null, totalPurchase: { $sum: "$purchase_amount" } } }]);

// Group by city with average purchase
db.users.aggregate([
  { $group: { _id: "$city", avgPurchase: { $avg: "$purchase_amount" } } },
  { $sort: { avgPurchase: -1 } }
]);

// Filter users above age 25, then group by city
db.users.aggregate([
  { $match: { age: { $gt: 25 } } },
  { $group: { _id: "$city", totalPurchase: { $sum: "$purchase_amount" } } }
]);

// Step 6: Indexing
// Create index on age
db.users.createIndex({ age: 1 });

// Create unique index on email
db.users.createIndex({ email: 1 }, { unique: true });

// Show all indexes
db.users.getIndexes();