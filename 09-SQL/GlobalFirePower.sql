-- Drop table if exists
DROP TABLE firepower;

-- Create new table to import data
CREATE TABLE firepower (
	country VARCHAR,
	ISO3 VARCHAR,
	rank INT,
	TotalPopulation INT,
	ManpowerAvailable INT,
	TotalMilitaryPersonnel INT,
	ActivePersonnel INT,
	ReservePersonnel INT,
	TotalAircraftStrength INT,
	FighterAircraft INT,
	AttackAircraft INT,
	TotalHelicopterStrength INT,
	AttackHelicopters INT
);

-- Import data from firepower.csv
-- View the table to ensure all data has been imported correctly
SELECT * FROM firepower;

DELETE FROM firepower WHERE "reservepersonnel" = 0;

UPDATE firepower SET
"fighteraircraft" = 1 WHERE firepower.fighteraircraft = 0;

SELECT ROUND(AVG(totalmilitarypersonnel),0) AS "Avg Total Military Personnel"
FROM firepower;

SELECT ROUND(AVG(TotalAircraftStrength),0) AS "Avg Total Aircraft Strength"
FROM firepower;

SELECT ROUND(AVG(TotalHelicopterStrength),0) AS "Avg Total Helicopter Strength"
FROM firepower;

SELECT ROUND(AVG(TotalPopulation),0) AS "Avg Total Population"
FROM firepower;