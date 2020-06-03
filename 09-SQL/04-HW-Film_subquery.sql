-- First select title and id for movie EARLY HOME
SELECT
	title
	,film_id
FROM
	film
WHERE
	title = 'ALTER VICTORY';

-- Using the film_id located in the previous query find it in the inventory table
SELECT
	*
FROM
	film_actor
WHERE
	film_id = 18;

-- Use subquery
SELECT
	*
FROM
	film_actor
WHERE
	film_id IN (
		SELECT
			film_id
		FROM
			film
		WHERE
			title = 'ALTER VICTORY'
	);
	


	
	

-- Use Join to find the inventory, film and store id
SELECT i.actor_id, i.film_id
FROM film_actor i
JOIN film f
ON (i.film_id = f.film_id)
WHERE f.title = 'ALTER VICTORY';

SELECT f.first_name, f.last_name
FROM film_actor i
JOIN actor f
ON (i.actor_id = f.actor_id)
WHERE i.film_id = '18';
-- Use Subquery to get the film_id from the query finding EARLY HOME
SELECT *
FROM actor
WHERE film_id IN
(
  SELECT film_id
  FROM film
  WHERE title = 'ALTER VICTORY'
);

-- Check to more sure the subquery returned correct value
SELECT *
FROM inventory
WHERE film_id IN (268);
