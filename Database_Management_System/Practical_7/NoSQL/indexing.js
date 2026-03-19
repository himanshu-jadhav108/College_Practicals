// ===============================
// INDEXING OPERATIONS
// ===============================

// Create indexes for faster queries

// Index on email (unique lookup)
db.users.createIndex({ email: 1 });

// Index on age (filtering)
db.users.createIndex({ age: 1 });

// Index on nested field (category inside purchases)
db.users.createIndex({ "purchases.category": 1 });

// Compound index (city + age)
db.users.createIndex({ city: 1, age: -1 });

// ===============================
// VIEW INDEXES
// ===============================
db.users.getIndexes();

// ===============================
// DROP INDEX (if needed)
// ===============================
db.users.dropIndex({ age: 1 });
