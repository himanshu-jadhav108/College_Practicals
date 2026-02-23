-- =============================================
-- Rollback Examples for Space Exploration Universe Database
-- =============================================
-- This script demonstrates various rollback scenarios in MySQL:
-- - Basic rollback after erroneous operations
-- - Partial rollback using savepoints
-- - Rollback in stored procedures
-- - Error simulation and recovery
-- Author: Himanshu Jadhav
-- Date: 2026
-- =============================================

-- Example 1: Basic rollback after accidental deletion
-- Demonstrates: START TRANSACTION, DELETE, ROLLBACK
START TRANSACTION;

-- Accidentally delete Earth (planet_id = 3)
DELETE FROM planet WHERE planet_id = 3;

-- Check what was deleted
SELECT * FROM planet WHERE name = 'Earth';

-- Oops! Rollback the deletion
ROLLBACK;

-- Verify Earth is back
SELECT * FROM planet WHERE name = 'Earth';

-- Example 2: Rollback after multiple operations
-- Demonstrates: Multiple operations before rollback
START TRANSACTION;

-- Insert a test galaxy
INSERT INTO galaxy (name, description, galaxy_type, age_in_millions_of_years, is_spherical)
VALUES ('Test Galaxy', 'Temporary test data', 'Spiral', 1000, TRUE);

-- Insert a test star
INSERT INTO star (name, galaxy_id, temperature, mass, is_visible)
VALUES ('Test Star', LAST_INSERT_ID(), 5000, 1.0, TRUE);

-- Insert a test planet
INSERT INTO planet (name, star_id, planet_type, has_life, distance_from_star)
VALUES ('Test Planet', LAST_INSERT_ID(), 'Rocky', FALSE, 100);

-- Realize this was just for testing, rollback everything
ROLLBACK;

-- Verify nothing was inserted
SELECT * FROM galaxy WHERE name = 'Test Galaxy';

-- Example 3: Partial rollback using savepoints
-- Demonstrates: SAVEPOINT, ROLLBACK TO SAVEPOINT
START TRANSACTION;

-- Insert valid mission
INSERT INTO space_mission (name, launch_year, agency, mission_type)
VALUES ('Valid Mission', 2025, 'NASA', 'Exploration');

SAVEPOINT mission_saved;

-- Insert planet visit (this might be invalid)
INSERT INTO mission_planet (mission_id, planet_id, visit_date)
VALUES (LAST_INSERT_ID(), 999, '2025-01-01');  -- Invalid planet_id

-- If the planet visit fails, rollback only that part
ROLLBACK TO SAVEPOINT mission_saved;

-- Commit the valid mission
COMMIT;

-- Example 4: Rollback in error simulation
-- Demonstrates: Forced error and rollback
DELIMITER //

CREATE PROCEDURE test_rollback()
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SELECT 'Error occurred, transaction rolled back' AS message;
    END;

    START TRANSACTION;

    -- Valid insert
    INSERT INTO comet (name, speed, is_periodic, description)
    VALUES ('Test Comet', 50, TRUE, 'Test data');

    -- Force an error (duplicate unique key)
    INSERT INTO comet (name, speed, is_periodic, description)
    VALUES ('Halley', 70, TRUE, 'Duplicate name - should fail');

    -- This point won't be reached due to error
    COMMIT;
END //

DELIMITER ;

-- Call the procedure to see rollback in action
CALL test_rollback();

-- Example 5: Rollback after constraint violation
-- Demonstrates: Foreign key constraint violation
START TRANSACTION;

-- Try to insert a planet with invalid star_id
INSERT INTO planet (name, star_id, planet_type, has_life, distance_from_star)
VALUES ('Invalid Planet', 99999, 'Rocky', FALSE, 100);

-- This will fail due to foreign key constraint
-- Transaction will be automatically rolled back by MySQL

-- Example 6: Manual rollback for business logic
-- Demonstrates: Conditional rollback based on business rules
START TRANSACTION;

-- Insert a mission
INSERT INTO space_mission (name, launch_year, agency, mission_type)
VALUES ('Future Mission', 2030, 'ESA', 'Research');

-- Check if launch year is in the future (business rule)
SET @mission_id = LAST_INSERT_ID();
SET @launch_year = (SELECT launch_year FROM space_mission WHERE mission_id = @mission_id);

IF @launch_year > YEAR(CURDATE()) THEN
    -- Future missions not allowed in current system
    SELECT 'Cannot add future missions' AS error_message;
    ROLLBACK;
ELSE
    COMMIT;
    SELECT 'Mission added successfully' AS success_message;
END IF;

-- Example 7: Rollback with cleanup
-- Demonstrates: Using rollback to clean up temporary data
START TRANSACTION;

-- Create temporary analysis data
CREATE TEMPORARY TABLE temp_analysis AS
SELECT g.name AS galaxy, COUNT(s.star_id) AS star_count
FROM galaxy g
LEFT JOIN star s ON g.galaxy_id = s.galaxy_id
GROUP BY g.galaxy_id, g.name;

-- Perform analysis
SELECT * FROM temp_analysis WHERE star_count > 1;

-- Clean up by rolling back (temporary tables are session-specific)
ROLLBACK;

-- Verify cleanup
SELECT COUNT(*) AS temp_tables_remaining
FROM information_schema.tables
WHERE table_name = 'temp_analysis' AND table_type = 'TEMPORARY';
