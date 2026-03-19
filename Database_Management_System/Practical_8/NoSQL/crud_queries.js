// Trending Hashtags
db.posts.aggregate([
  { $unwind: "$hashtags" },
  { $group: { _id: "$hashtags", count: { $sum: 1 } } },
  { $sort: { count: -1 } },
  { $limit: 5 },
]);

// Most Liked Posts
db.posts.find().sort({ likes: -1 }).limit(5);

// Engagement by Hashtag
db.posts.aggregate([
  { $unwind: "$hashtags" },
  {
    $group: {
      _id: "$hashtags",
      total_likes: { $sum: "$likes" },
    },
  },
]);
