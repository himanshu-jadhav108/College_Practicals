-- =============================================
-- Space Exploration Universe Database Schema
-- =============================================
-- This script creates the database schema for the Space Exploration Universe Database System.
-- It includes tables for galaxies, stars, planets, moons, comets, space missions, and mission-planet relationships.
-- Normalization: 3NF (Third Normal Form)
-- Relationships: One-to-Many and Many-to-Many
-- Author: Himanshu Jadhav
-- Date: 2026
-- =============================================

-- Galaxy table: Represents astronomical galaxies
CREATE TABLE galaxy (
  galaxy_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each galaxy',
  name VARCHAR(100) UNIQUE NOT NULL COMMENT 'Name of the galaxy',
  description TEXT NOT NULL COMMENT 'Detailed description of the galaxy',
  galaxy_type VARCHAR(50) COMMENT 'Type of galaxy (e.g., Spiral, Elliptical)',
  age_in_millions_of_years INT NOT NULL COMMENT 'Age of the galaxy in millions of years',
  is_spherical BOOLEAN NOT NULL COMMENT 'Whether the galaxy is spherical in shape'
);

-- Star table: Represents stars within galaxies
CREATE TABLE star (
  star_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each star',
  name VARCHAR(100) UNIQUE NOT NULL COMMENT 'Name of the star',
  galaxy_id INT NOT NULL COMMENT 'Reference to the galaxy containing this star',
  temperature INT COMMENT 'Surface temperature of the star in Kelvin',
  mass DECIMAL(10,2) COMMENT 'Mass of the star in solar masses',
  is_visible BOOLEAN NOT NULL COMMENT 'Whether the star is visible from Earth',
  FOREIGN KEY (galaxy_id) REFERENCES galaxy(galaxy_id) ON DELETE CASCADE
);

-- Planet table: Represents planets orbiting stars
CREATE TABLE planet (
  planet_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each planet',
  name VARCHAR(100) UNIQUE NOT NULL COMMENT 'Name of the planet',
  star_id INT NOT NULL COMMENT 'Reference to the star this planet orbits',
  planet_type VARCHAR(50) COMMENT 'Type of planet (e.g., Rocky, Gas Giant)',
  has_life BOOLEAN NOT NULL COMMENT 'Whether the planet has life',
  distance_from_star INT COMMENT 'Distance from the star in AU (Astronomical Units)',
  FOREIGN KEY (star_id) REFERENCES star(star_id) ON DELETE CASCADE
);

-- Moon table: Represents moons orbiting planets
CREATE TABLE moon (
  moon_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each moon',
  name VARCHAR(100) UNIQUE NOT NULL COMMENT 'Name of the moon',
  planet_id INT NOT NULL COMMENT 'Reference to the planet this moon orbits',
  is_spherical BOOLEAN NOT NULL COMMENT 'Whether the moon is spherical',
  age_in_millions_of_years INT COMMENT 'Age of the moon in millions of years',
  FOREIGN KEY (planet_id) REFERENCES planet(planet_id) ON DELETE CASCADE
);

-- Comet table: Represents independent celestial objects (comets)
CREATE TABLE comet (
  comet_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each comet',
  name VARCHAR(100) UNIQUE NOT NULL COMMENT 'Name of the comet',
  speed INT NOT NULL COMMENT 'Speed of the comet in km/s',
  is_periodic BOOLEAN NOT NULL COMMENT 'Whether the comet is periodic',
  description TEXT COMMENT 'Additional description of the comet'
);

-- Space Mission table: Represents space exploration missions
CREATE TABLE space_mission (
  mission_id INT AUTO_INCREMENT PRIMARY KEY COMMENT 'Unique identifier for each mission',
  name VARCHAR(100) UNIQUE NOT NULL COMMENT 'Name of the mission',
  launch_year INT NOT NULL COMMENT 'Year the mission was launched',
  agency VARCHAR(100) NOT NULL COMMENT 'Space agency conducting the mission',
  mission_type VARCHAR(50) NOT NULL COMMENT 'Type of mission (e.g., Exploration, Research)'
);

-- Mission-Planet junction table: Many-to-Many relationship between missions and planets
CREATE TABLE mission_planet (
  mission_id INT NOT NULL COMMENT 'Reference to the mission',
  planet_id INT NOT NULL COMMENT 'Reference to the planet visited',
  visit_date DATE COMMENT 'Date of the planet visit',
  PRIMARY KEY (mission_id, planet_id),
  FOREIGN KEY (mission_id) REFERENCES space_mission(mission_id) ON DELETE CASCADE,
  FOREIGN KEY (planet_id) REFERENCES planet(planet_id) ON DELETE CASCADE
);

-- Indexes for performance optimization
CREATE INDEX idx_star_galaxy ON star(galaxy_id) COMMENT 'Index on galaxy_id for faster galaxy-star joins';
CREATE INDEX idx_planet_star ON planet(star_id) COMMENT 'Index on star_id for faster star-planet joins';
CREATE INDEX idx_moon_planet ON moon(planet_id) COMMENT 'Index on planet_id for faster planet-moon joins';
CREATE INDEX idx_planet_life ON planet(has_life) COMMENT 'Index on has_life for fast habitability filtering';