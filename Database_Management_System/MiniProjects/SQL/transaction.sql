-- =============================================
-- Transaction Examples for Space Exploration Universe Database
-- =============================================
-- This script demonstrates ACID properties in MySQL transactions:
-- Atomicity, Consistency, Isolation, Durability
-- Includes examples of COMMIT, ROLLBACK, and error handling
-- Author: Himanshu Jadhav
-- Date: 2026
-- =============================================

-- Example 1: Successful mission insertion with planet visit
-- Demonstrates: START TRANSACTION, INSERT, LAST_INSERT_ID(), COMMIT
START TRANSACTION;

-- Insert a new space mission
INSERT INTO space_mission (name, launch_year, agency, mission_type)
VALUES ('Deep Survey', 2026, 'ISRO', 'Research');

-- Link the mission to a planet visit
INSERT INTO mission_planet (mission_id, planet_id, visit_date)
VALUES (LAST_INSERT_ID(), 3, '2026-07-10');

-- Commit the transaction
COMMIT;

-- Example 2: Transaction with multiple operations
-- Demonstrates: Multiple INSERTs in a single transaction
START TRANSACTION;

-- Insert a new galaxy
INSERT INTO galaxy (name, description, galaxy_type, age_in_millions_of_years, is_spherical)
VALUES ('New Galaxy', 'A newly discovered galaxy', 'Spiral', 5000, TRUE);

-- Insert a star in that galaxy
INSERT INTO star (name, galaxy_id, temperature, mass, is_visible)
VALUES ('New Star', LAST_INSERT_ID(), 6000, 1.5, TRUE);

-- Insert a planet orbiting the star
INSERT INTO planet (name, star_id, planet_type, has_life, distance_from_star)
VALUES ('New Planet', LAST_INSERT_ID(), 'Rocky', FALSE, 200);

COMMIT;

-- Example 3: Transaction with SAVEPOINT and partial rollback
-- Demonstrates: SAVEPOINT, ROLLBACK TO SAVEPOINT
START TRANSACTION;

-- Insert mission
INSERT INTO space_mission (name, launch_year, agency, mission_type)
VALUES ('Test Mission', 2025, 'NASA', 'Test');

SAVEPOINT mission_inserted;

-- Insert planet visit
INSERT INTO mission_planet (mission_id, planet_id, visit_date)
VALUES (LAST_INSERT_ID(), 1, '2025-01-01');

-- Simulate an error condition
-- If something goes wrong here, we can rollback to the savepoint
-- For demonstration, we'll rollback to savepoint
ROLLBACK TO SAVEPOINT mission_inserted;

-- Now commit only the mission (planet visit was rolled back)
COMMIT;

-- Example 4: Error handling with transaction rollback
-- Demonstrates: Conditional rollback based on error
DELIMITER //

CREATE PROCEDURE safe_mission_insert(
    IN mission_name VARCHAR(100),
    IN launch_year INT,
    IN agency_name VARCHAR(100),
    IN mission_type VARCHAR(50),
    IN planet_id INT,
    IN visit_date DATE
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Rollback on any SQL error
        ROLLBACK;
        SELECT 'Transaction rolled back due to error' AS status;
    END;

    START TRANSACTION;

    -- Insert mission
    INSERT INTO space_mission (name, launch_year, agency, mission_type)
    VALUES (mission_name, launch_year, agency_name, mission_type);

    -- Insert planet visit
    INSERT INTO mission_planet (mission_id, planet_id, visit_date)
    VALUES (LAST_INSERT_ID(), planet_id, visit_date);

    COMMIT;
    SELECT 'Mission inserted successfully' AS status;
END //

DELIMITER ;

-- Call the procedure
CALL safe_mission_insert('Safe Mission', 2027, 'ESA', 'Observation', 2, '2027-05-15');

-- Example 5: Batch transaction for multiple related inserts
-- Demonstrates: Bulk operations within transaction
START TRANSACTION;

-- Insert multiple comets at once
INSERT INTO comet (name, speed, is_periodic, description) VALUES
('Comet A', 50, TRUE, 'New periodic comet'),
('Comet B', 60, FALSE, 'Long-period comet'),
('Comet C', 45, TRUE, 'Short-period comet');

-- Verify insertion
SELECT COUNT(*) AS new_comets_added FROM comet WHERE name IN ('Comet A', 'Comet B', 'Comet C');

COMMIT;

-- Example 6: Read-only transaction for consistency
-- Demonstrates: Consistent reads across multiple queries
START TRANSACTION READ ONLY;

-- Multiple SELECT queries that need consistent data
SELECT COUNT(*) AS total_galaxies FROM galaxy;
SELECT COUNT(*) AS total_stars FROM star;
SELECT COUNT(*) AS total_planets FROM planet;

COMMIT;
