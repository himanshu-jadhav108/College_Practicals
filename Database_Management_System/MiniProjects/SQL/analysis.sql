-- =============================================
-- Analytical Queries for Space Exploration Universe Database
-- =============================================
-- This script contains various analytical SQL queries demonstrating:
-- - Aggregation and grouping
-- - Joins and subqueries
-- - Window functions
-- - Ranking and statistical analysis
-- - Performance optimization techniques
-- Author: Himanshu Jadhav
-- Date: 2026
-- =============================================

-- Query 1: Galaxy with the highest average star temperature
-- Demonstrates: JOIN, GROUP BY, AVG, ORDER BY, LIMIT
SELECT
    g.name AS galaxy_name,
    ROUND(AVG(s.temperature), 2) AS avg_temperature_kelvin,
    COUNT(s.star_id) AS star_count
FROM galaxy g
JOIN star s ON g.galaxy_id = s.galaxy_id
GROUP BY g.galaxy_id, g.name
ORDER BY avg_temperature_kelvin DESC
LIMIT 1;

-- Query 2: Planet with the most moons
-- Demonstrates: LEFT JOIN, GROUP BY, COUNT, ORDER BY, LIMIT
SELECT
    p.name AS planet_name,
    COUNT(m.moon_id) AS moon_count,
    s.name AS star_name
FROM planet p
LEFT JOIN moon m ON p.planet_id = m.planet_id
JOIN star s ON p.star_id = s.star_id
GROUP BY p.planet_id, p.name, s.name
ORDER BY moon_count DESC
LIMIT 1;

-- Query 3: Habitability distribution across galaxies
-- Demonstrates: JOIN, GROUP BY, SUM, COUNT, calculated fields
SELECT
    g.name AS galaxy_name,
    COUNT(p.planet_id) AS total_planets,
    SUM(p.has_life) AS habitable_planets,
    ROUND((SUM(p.has_life) / COUNT(p.planet_id)) * 100, 2) AS habitability_percentage
FROM galaxy g
JOIN star s ON g.galaxy_id = s.galaxy_id
JOIN planet p ON s.star_id = p.star_id
GROUP BY g.galaxy_id, g.name
ORDER BY habitability_percentage DESC;

-- Query 4: Rank stars by temperature using window function
-- Demonstrates: Window functions (RANK), ORDER BY in window
SELECT
    s.name AS star_name,
    s.temperature AS temperature_kelvin,
    g.name AS galaxy_name,
    RANK() OVER (ORDER BY s.temperature DESC) AS temperature_rank
FROM star s
JOIN galaxy g ON s.galaxy_id = g.galaxy_id
ORDER BY temperature_rank;

-- Query 5: Most active space agency by mission count
-- Demonstrates: GROUP BY, COUNT, ORDER BY
SELECT
    agency,
    COUNT(*) AS mission_count,
    GROUP_CONCAT(name ORDER BY launch_year) AS mission_names
FROM space_mission
GROUP BY agency
ORDER BY mission_count DESC;

-- Query 6: Planets visited by missions with mission details
-- Demonstrates: Multiple JOINs, DATE formatting
SELECT
    p.name AS planet_name,
    sm.name AS mission_name,
    sm.agency,
    sm.mission_type,
    DATE_FORMAT(mp.visit_date, '%M %d, %Y') AS visit_date_formatted
FROM mission_planet mp
JOIN planet p ON mp.planet_id = p.planet_id
JOIN space_mission sm ON mp.mission_id = sm.mission_id
ORDER BY mp.visit_date;

-- Query 7: Statistical summary of celestial objects
-- Demonstrates: UNION ALL, subqueries, aggregation
SELECT 'Galaxies' AS object_type, COUNT(*) AS count FROM galaxy
UNION ALL
SELECT 'Stars' AS object_type, COUNT(*) AS count FROM star
UNION ALL
SELECT 'Planets' AS object_type, COUNT(*) AS count FROM planet
UNION ALL
SELECT 'Moons' AS object_type, COUNT(*) AS count FROM moon
UNION ALL
SELECT 'Comets' AS object_type, COUNT(*) AS count FROM comet
UNION ALL
SELECT 'Missions' AS object_type, COUNT(*) AS count FROM space_mission;

-- Query 8: Planets with their star and galaxy hierarchy
-- Demonstrates: Multiple JOINs, hierarchical data
SELECT
    CONCAT(g.name, ' → ', s.name, ' → ', p.name) AS celestial_hierarchy,
    p.planet_type,
    p.has_life,
    p.distance_from_star
FROM planet p
JOIN star s ON p.star_id = s.star_id
JOIN galaxy g ON s.galaxy_id = g.galaxy_id
ORDER BY g.name, s.name, p.distance_from_star;

-- Query 9: Average distance analysis by planet type
-- Demonstrates: GROUP BY, AVG, HAVING
SELECT
    planet_type,
    COUNT(*) AS planet_count,
    ROUND(AVG(distance_from_star), 2) AS avg_distance_from_star,
    MIN(distance_from_star) AS min_distance,
    MAX(distance_from_star) AS max_distance
FROM planet
GROUP BY planet_type
HAVING planet_count > 1
ORDER BY avg_distance_from_star;

-- Query 10: Mission timeline analysis
-- Demonstrates: Subqueries, DATE functions
SELECT
    YEAR(visit_date) AS visit_year,
    COUNT(*) AS visits_count,
    GROUP_CONCAT(DISTINCT sm.agency) AS agencies_involved
FROM mission_planet mp
JOIN space_mission sm ON mp.mission_id = sm.mission_id
GROUP BY YEAR(visit_date)
ORDER BY visit_year;

-- Query 11: Performance analysis - EXPLAIN example
-- (Uncomment to run: This shows query execution plan)
EXPLAIN SELECT g.name, COUNT(s.star_id) AS star_count
FROM galaxy g
JOIN star s ON g.galaxy_id = s.galaxy_id
GROUP BY g.galaxy_id, g.name;

-- Query 12: Advanced ranking with dense rank and row number
-- Demonstrates: Multiple window functions
SELECT
    s.name AS star_name,
    s.temperature,
    RANK() OVER (ORDER BY s.temperature DESC) AS temp_rank,
    DENSE_RANK() OVER (ORDER BY s.temperature DESC) AS temp_dense_rank,
    ROW_NUMBER() OVER (ORDER BY s.temperature DESC) AS temp_row_num
FROM star s
ORDER BY temp_rank;
