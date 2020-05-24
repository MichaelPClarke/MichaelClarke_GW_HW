CREATE VIEW title_count	as

select f.title, count(i.film_id) as Copies
FROM inventory i
INNER JOIN film f
ON (i.film_id = f.film_id)
group by title;

select * from title_count
WHERE Copies = 7