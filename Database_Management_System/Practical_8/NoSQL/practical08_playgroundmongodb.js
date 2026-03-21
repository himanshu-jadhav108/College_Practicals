// MongoDB Playground for Practical 08
// Case Study: Social Media Data Processing using NoSQL
// Maintainer: Himanshu Jadhav

// Step 1: Create and switch to the database
const database = "practical08";
const collection = "posts";

use(database);

// Step 2: Create the 'posts' collection
db.createCollection(collection);

// Step 3: Insert sample social media posts (anime characters as users)
db.posts.insertMany([
  {
    user: { username: "Naruto Uzumaki", verified: true, location: "Konoha" },
    text: "Believe it! Training hard today.",
    hashtags: ["#ninja", "#training", "#believeit"],
    engagement: { likes: 120, comments: 15, shares: 10 },
    created_at: new Date("2026-03-20T10:00:00Z")
  },
  {
    user: { username: "Sasuke Uchiha", verified: false, location: "Konoha" },
    text: "Power comes from revenge.",
    hashtags: ["#uchiha", "#revenge"],
    engagement: { likes: 200, comments: 30, shares: 25 },
    created_at: new Date("2026-03-20T11:00:00Z")
  },
  {
    user: { username: "Eren Yeager", verified: true, location: "Shiganshina" },
    text: "Fight for freedom!",
    hashtags: ["#freedom", "#titans", "#paradise"],
    engagement: { likes: 500, comments: 80, shares: 60 },
    created_at: new Date("2026-03-19T09:30:00Z")
  },
  {
    user: { username: "Light Yagami", verified: false, location: "Tokyo" },
    text: "Justice will prevail.",
    hashtags: ["#justice", "#kira"],
    engagement: { likes: 350, comments: 40, shares: 20 },
    created_at: new Date("2026-03-18T14:15:00Z")
  },
  {
    user: { username: "Ichigo Kurosaki", verified: true, location: "Karakura" },
    text: "Protecting my friends always.",
    hashtags: ["#shinigami", "#friends"],
    engagement: { likes: 220, comments: 25, shares: 15 },
    created_at: new Date("2026-03-17T16:45:00Z")
  }
]);

// Step 4: CRUD Operations
// Read all posts
db.posts.find();

// Update engagement (Naruto gets more likes)
db.posts.updateOne(
  { "user.username": "Naruto Uzumaki" },
  { $set: { "engagement.likes": 150 } }
);

// Delete Light Yagami's post
db.posts.deleteOne({ "user.username": "Light Yagami" });

// Step 5: Aggregation Examples
// Trending hashtags (unwind + group + sort + limit)
db.posts.aggregate([
  { $unwind: "$hashtags" },
  { $group: { _id: "$hashtags", count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $limit: 5 }
]);

// Engagement analysis: average likes per user
db.posts.aggregate([
  { $group: { _id: "$user.username", avgLikes: { $avg: "$engagement.likes" } } },
  { $sort: { avgLikes: -1 } }
]);

// Top users by shares
db.posts.aggregate([
  { $group: { _id: "$user.username", totalShares: { $sum: "$engagement.shares" } } },
  { $sort: { totalShares: -1 } },
  { $limit: 3 }
]);

// Filter posts by location (Konoha)
db.posts.find({ "user.location": "Konoha" });

// Step 6: Indexing
// Create index on hashtags
db.posts.createIndex({ hashtags: 1 });

// Create index on likes
db.posts.createIndex({ "engagement.likes": 1 });

// Create index on username
db.posts.createIndex({ "user.username": 1 });

// Create index on timestamp
db.posts.createIndex({ created_at: 1 });

// Show all indexes
db.posts.getIndexes();