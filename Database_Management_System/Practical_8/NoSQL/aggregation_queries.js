// ===============================
// AGGREGATION QUERIES
// ===============================

// 1. Top Trending Hashtags
db.posts.aggregate([
  { $unwind: "$hashtags" },
  {
    $group: {
      _id: "$hashtags",
      count: { $sum: 1 },
    },
  },
  { $sort: { count: -1 } },
  { $limit: 5 },
]);

// 2. Total Engagement per Hashtag
db.posts.aggregate([
  { $unwind: "$hashtags" },
  {
    $group: {
      _id: "$hashtags",
      total_likes: { $sum: "$likes" },
      total_comments: { $sum: "$comments" },
    },
  },
]);

// 3. Top Users by Likes
db.posts.aggregate([
  {
    $group: {
      _id: "$user.username",
      total_likes: { $sum: "$likes" },
    },
  },
  { $sort: { total_likes: -1 } },
]);

// 4. Monthly Post Count
db.posts.aggregate([
  {
    $group: {
      _id: { $month: { $toDate: "$created_at" } },
      total_posts: { $sum: 1 },
    },
  },
]);
