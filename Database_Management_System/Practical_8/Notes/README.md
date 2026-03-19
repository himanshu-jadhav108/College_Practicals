# Practical 8 — Case Study: Social Media Data Processing using NoSQL

## Problem Statement

Social media platforms generate massive unstructured/semi-structured data (posts, comments, interactions). Relational databases struggle due to rigid schemas and joins. MongoDB, a NoSQL database, provides flexible schemas, scalability, and efficient querying for social media analytics.

## Objective

- Design a flexible data model for posts + metadata
- Perform CRUD and analytical queries
- Use aggregation + indexing for insights

## Data Model

- Collection: **posts**
- Fields: user info (embedded), post text, hashtags (array), engagement (likes, comments, shares), timestamp, location, verification
- Embedded user details → faster reads
- Arrays for hashtags → trend analysis

## Relationships

- Embedding avoids joins, improves read performance
- Trade-off: duplication if user details change
- Optimized for read-heavy analytics workloads

## Theory

- MongoDB stores data in collections/documents (JSON-like)
- CRUD: insert, retrieve, update, delete posts
- Aggregation: pipeline stages (unwind, group, sort, limit) for insights like trending hashtags, engagement metrics
- Indexing: improves query speed on hashtags, timestamps, likes, usernames

## Operations Overview

- Created **posts** collection, imported dataset
- CRUD operations performed
- Queries: filter by location, likes, hashtags
- Aggregation: trending hashtags, engagement analysis, top users
- Indexes applied on `hashtags`, `likes`, `user.username`, `created_at`

## Aggregation Pipeline

1. **Unwind** hashtags array
2. **Group** by hashtags/users → metrics
3. **Sort** results (e.g., top hashtags)
4. **Limit** output (e.g., top 5)

## Indexing Strategy

- Fields: `hashtags`, `likes`, `user.username`, `created_at`
- Benefits: faster queries, efficient filtering/sorting, optimized analytics

## Notes

- Tools: MongoDB Atlas / Compass
- Data in JSON format
- Demonstrated CRUD, aggregation, indexing
- Showcased handling of unstructured/semi-structured data
- Real-world social media analytics use case

# Maintainer Section

Maintained by **Himanshu Jadhav**
Second-Year Engineering Student (AI & Data Science)

[GitHub](https://github.com/himanshu-jadhav108) • [LinkedIn](https://www.linkedin.com/in/himanshu-jadhav-328082339) • [Instagram](https://www.instagram.com/himanshu_jadhav_108?igsh=MWYxamppcTBlY3Rl) • [Portfolio](https://himanshu-jadhav-portfolio.vercel.app/)

---
