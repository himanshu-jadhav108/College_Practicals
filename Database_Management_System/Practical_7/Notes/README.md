# Practical 7 — NoSQL Database Introduction: MongoDB Aggregation and Indexing

## Problem Statement

Modern applications generate large volumes of semi/unstructured data that relational databases struggle to handle due to rigid schemas. MongoDB, a NoSQL document-oriented database, offers flexible JSON-like storage, efficient CRUD operations, aggregation for analysis, and indexing for performance.

## Objective

- Understand MongoDB’s flexible schema and CRUD operations
- Explore aggregation pipelines for analysis
- Apply indexing to optimize queries

## Data Model

- Collection: **users**
- Fields: `name`, `age`, `email`, `city`, `purchase_amount`
- JSON-like documents allow schema flexibility
- Relationships:
  - **Embedding** (e.g., address inside user document) → faster reads
  - **Referencing** (IDs of related docs) → less duplication, more query complexity

## Theory

- MongoDB stores data in collections/documents, not tables/rows
- CRUD: insert, retrieve, update, delete
- Aggregation: pipeline stages (filter, group, sort, project) for computations like averages, totals
- Indexing: improves query speed on frequently accessed fields (`age`, `email`)
- Denormalization: related data stored together for performance, with some redundancy

## Operations Overview

- Created **users** collection
- Inserted documents with user details
- Performed CRUD operations
- Aggregation examples:
  - Average age
  - Total purchase amounts
  - Group by city
- Indexes applied on `age` and `email` for faster queries

## Aggregation Pipeline

1. **Filter**: e.g., users above certain age
2. **Group**: by city, compute sums/averages
3. **Sort**: by totals or averages
4. **Project**: select required fields

## Indexing Strategy

- Fields: `age`, `email`
- Benefits: fewer documents scanned, faster queries, efficient sorting

## Notes

- Tools: MongoDB Atlas / Compass
- Data in JSON format
- CRUD, aggregation, and indexing demonstrated
- Highlights differences from relational databases

# Maintainer Section

Maintained by **Himanshu Jadhav**
Second-Year Engineering Student (AI & Data Science)

[GitHub](https://github.com/himanshu-jadhav108) • [LinkedIn](https://www.linkedin.com/in/himanshu-jadhav-328082339) • [Instagram](https://www.instagram.com/himanshu_jadhav_108?igsh=MWYxamppcTBlY3Rl) • [Portfolio](https://himanshu-jadhav-portfolio.vercel.app/)

---
