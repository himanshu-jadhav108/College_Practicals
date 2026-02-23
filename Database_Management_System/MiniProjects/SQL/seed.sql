-- =============================================
-- Seed Data for Space Exploration Universe Database
-- =============================================
-- This script populates the database with sample data for demonstration purposes.
-- It includes realistic astronomical data for galaxies, stars, planets, moons, comets, and missions.
-- Author: Himanshu Jadhav
-- Date: 2026
-- =============================================

-- Insert sample galaxies
INSERT INTO galaxy (galaxy_id, name, description, galaxy_type, age_in_millions_of_years, is_spherical) VALUES
(1, 'Milky Way', 'Our home galaxy containing the Solar System', 'Spiral', 13600, TRUE),
(2, 'Andromeda', 'Nearest large galaxy to the Milky Way', 'Spiral', 10000, TRUE),
(3, 'Triangulum', 'Small spiral galaxy in the Local Group', 'Spiral', 8000, TRUE),
(4, 'Whirlpool', 'Interacting galaxy with prominent spiral arms', 'Spiral', 9000, TRUE),
(5, 'Sombrero', 'Galaxy with a bright central bulge', 'Elliptical', 11000, TRUE),
(6, 'Cartwheel', 'Ring galaxy formed by a collision', 'Ring', 5000, FALSE);

-- Insert sample stars
INSERT INTO star (star_id, name, galaxy_id, temperature, mass, is_visible) VALUES
(1, 'Sun', 1, 5500, 1.00, TRUE),
(2, 'Sirius', 1, 9900, 2.10, TRUE),
(3, 'Betelgeuse', 2, 3500, 20.00, TRUE),
(4, 'Rigel', 2, 11000, 18.00, TRUE),
(5, 'Vega', 3, 9600, 2.10, TRUE),
(6, 'Polaris', 4, 6000, 5.40, TRUE);

-- Insert sample planets
INSERT INTO planet (planet_id, name, star_id, planet_type, has_life, distance_from_star) VALUES
(1, 'Mercury', 1, 'Rocky', FALSE, 58),
(2, 'Venus', 1, 'Rocky', FALSE, 108),
(3, 'Earth', 1, 'Rocky', TRUE, 150),
(4, 'Mars', 1, 'Rocky', FALSE, 228),
(5, 'Jupiter', 1, 'Gas Giant', FALSE, 778),
(6, 'Saturn', 1, 'Gas Giant', FALSE, 1430),
(7, 'Uranus', 1, 'Ice Giant', FALSE, 2870),
(8, 'Neptune', 1, 'Ice Giant', FALSE, 4500),
(9, 'PlanetX', 2, 'Gas', FALSE, 300),
(10, 'PlanetY', 3, 'Rocky', FALSE, 400),
(11, 'PlanetZ', 4, 'Gas', FALSE, 500),
(12, 'PlanetK', 5, 'Ice', FALSE, 600);

-- Insert sample moons
INSERT INTO moon (moon_id, name, planet_id, is_spherical, age_in_millions_of_years) VALUES
(1, 'Moon', 3, TRUE, 4500),
(2, 'Phobos', 4, FALSE, 1000),
(3, 'Deimos', 4, FALSE, 1000),
(4, 'Io', 5, TRUE, 4500),
(5, 'Europa', 5, TRUE, 4500),
(6, 'Ganymede', 5, TRUE, 4500),
(7, 'Callisto', 5, TRUE, 4500),
(8, 'Titan', 6, TRUE, 4500),
(9, 'Rhea', 6, TRUE, 4500),
(10, 'Iapetus', 6, TRUE, 4500),
(11, 'Miranda', 7, TRUE, 4500),
(12, 'Ariel', 7, TRUE, 4500),
(13, 'Umbriel', 7, TRUE, 4500),
(14, 'Triton', 8, TRUE, 4500),
(15, 'Nereid', 8, FALSE, 4500),
(16, 'MoonA', 9, TRUE, 2000),
(17, 'MoonB', 10, FALSE, 2000),
(18, 'MoonC', 11, TRUE, 2000),
(19, 'MoonD', 12, TRUE, 2000),
(20, 'MoonE', 1, TRUE, 2000);

-- Insert sample comets
INSERT INTO comet (comet_id, name, speed, is_periodic, description) VALUES
(1, 'Halley', 70, TRUE, 'Famous periodic comet visible from Earth every 76 years'),
(2, 'Hale-Bopp', 44, FALSE, 'Bright comet discovered in 1995'),
(3, 'Encke', 69, TRUE, 'Short-period comet with 3.3 year orbit');

-- Insert sample space missions
INSERT INTO space_mission (mission_id, name, launch_year, agency, mission_type) VALUES
(1, 'Voyager 1', 1977, 'NASA', 'Exploration'),
(2, 'Mars Reconnaissance Orbiter', 2005, 'NASA', 'Orbiter'),
(3, 'ExoSearch', 2022, 'ESA', 'Research');

-- Insert mission-planet relationships
INSERT INTO mission_planet (mission_id, planet_id, visit_date) VALUES
(1, 5, '1979-03-05'),  -- Voyager 1 flyby of Jupiter
(1, 6, '1980-11-12'),  -- Voyager 1 flyby of Saturn
(2, 4, '2006-03-10'),  -- MRO arrival at Mars
(3, 3, '2023-06-21');  -- ExoSearch observation of Earth
