// ===============================
// BASIC QUERIES
// ===============================

// Get all posts
db.posts.find();

// Filter posts with likes > 100
db.posts.find({ likes: { $gt: 100 } });

// Find posts with specific hashtag
db.posts.find({ hashtags: "MongoDB" });

// Find posts by verified users
db.posts.find({ is_verified: true });

// Sort posts by likes
db.posts.find().sort({ likes: -1 });

// Limit results
db.posts.find().limit(5);
