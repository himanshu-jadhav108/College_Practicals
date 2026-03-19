// ===============================
// AGGREGATION QUERIES
// ===============================

// 1. Total Sales Across All Users
db.users.aggregate([
  { $unwind: "$purchases" },
  {
    $group: {
      _id: null,
      total_sales: { $sum: "$purchases.amount" },
    },
  },
]);

// 2. Average Age of Users
db.users.aggregate([
  {
    $group: {
      _id: null,
      avg_age: { $avg: "$age" },
    },
  },
]);

// 3. Total Sales by Category
db.users.aggregate([
  { $unwind: "$purchases" },
  {
    $group: {
      _id: "$purchases.category",
      total_sales: { $sum: "$purchases.amount" },
    },
  },
  { $sort: { total_sales: -1 } },
]);

// 4. Top Spending Users
db.users.aggregate([
  { $unwind: "$purchases" },
  {
    $group: {
      _id: "$name",
      total_spent: { $sum: "$purchases.amount" },
    },
  },
  { $sort: { total_spent: -1 } },
]);

// 5. Users Count by City
db.users.aggregate([
  {
    $group: {
      _id: "$city",
      count: { $sum: 1 },
    },
  },
]);
