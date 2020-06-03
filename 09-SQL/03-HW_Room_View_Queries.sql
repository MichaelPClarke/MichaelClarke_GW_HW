-- Using a subquery 
SELECT title,
(SELECT COUNT(inventory.film_id)
	FROM inventory
	WHERE film.film_id = inventory.film_id ) AS number_of_copies
FROM film;

-- Create View
CREATE VIEW title_count AS 

SELECT
	title
	,COUNT(i.film_id) AS number_of_films
FROM
	film f
	INNER JOIN inventory i
	ON f.film_id = i.film_id
GROUP BY
	title;
-- Query the view to the titles with 7 copies
SELECT
	title
	, number_of_films
FROM
	title_count
WHERE
	number_of_films = 7;