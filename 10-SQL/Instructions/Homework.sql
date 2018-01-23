use sakila;

-- * 1a. Display the first and last names of all actors from the table `actor`.
-- 
select first_name, last_name from actor;

-- * 1b. Display the first and last name of each actor in a single column in upper case letters. 
-- Name the column `Actor Name`. 

select concat (first_name,' ',last_name) Actor_Name
from actor;

-- * 2a. You need to find the ID number, first name, and last name of an actor, 
-- of whom you know only the first name, "Joe." What is one query would you 
-- use to obtain this information?

SELECT actor_id, first_name, last_name
FROM actor
WHERE first_name='Joe';

-- * 2b. Find all actors whose last name contain the letters `GEN`:

SELECT first_name,last_name
FROM actor
WHERE last_name like '%GEN%';

-- * 2c. Find all actors whose last names contain the letters `LI`. 
-- This time, order the rows by last name and first name, in that order:

SELECT last_name,first_name 
FROM actor
WHERE last_name like '%LI%';

-- * 2d. Using `IN`, display the `country_id` and `country` columns of the 
-- following countries: Afghanistan, Bangladesh, and China:
--
SELECT country_id, country
FROM country
WHERE country IN ('Afghanistan','Bangladesh','China');

-- * 3a. Add a `middle_name` column to the table `actor`. 
-- Position it between `first_name` and `last_name`. 
-- Hint: you will need to specify the data type.

ALTER TABLE actor ADD middle_name VARCHAR(60) AFTER first_name;

-- * 3b. You realize that some of these actors have tremendously long last names. 
-- Change the data type of the `middle_name` column to `blobs`.

ALTER TABLE actor MODIFY middle_name blob;

-- * 3c. Now delete the `middle_name` column.

ALTER TABLE actor DROP COLUMN middle_name;

-- * 4a. List the last names of actors, as well as how many actors have that last name.

SELECT last_name, count(last_name) 
FROM actor
GROUP by last_name;
 
--  * 4b. List last names of actors and the number of actors who have that last name, 
--  but only for names that are shared by at least two actors

SELECT last_name, count(last_name)
WHERE count(last_name) =>2
FROM actor 
GROUP by last_name;
 
-- * 4c. Oh, no! The actor `HARPO WILLIAMS` was accidentally 
-- entered in the `actor` table as `GROUCHO WILLIAMS`, 
-- the name of Harpo's second cousin's husband's yoga teacher. Write a query to fix the record.

UPDATE actor
SET 
    first_name = 'Harpo'
WHERE
    first_name = 'GROUCHO' and last_name = 'WILLIAMS';
    
-- * 4d. Perhaps we were too hasty in changing `GROUCHO` to `HARPO`. 
-- It turns out that `GROUCHO` was the correct name after all! In a single query, 
-- if the first name of the actor is currently `HARPO`, change it to `GROUCHO`. 
-- Otherwise, change the first name to `MUCHO GROUCHO`, as that is exactly 
-- what the actor will be with the grievous error. BE CAREFUL NOT TO CHANGE 
-- THE FIRST NAME OF EVERY ACTOR TO `MUCHO GROUCHO`, 
-- HOWEVER! (Hint: update the record using a unique identifier.)
    
UPDATE actor
SET 
    first_name = 'MUCHO GROUCHO'
WHERE
    first_name = 'HARPO' and last_name = 'WILLIAMS';
    
-- * 5a. You cannot locate the schema of the `address` table. 
-- Which query would you use to re-create it?

CREATE TABLE ADDRESS(
    
id INTEGER(11) AUTO_INCREMENT NOT NULL,
address VARCHAR(30) NOT NULL,
address2 VARCHAR(30) NOT NULL,
district INTEGER(10),
city_id VARCHAR(30) NOT NULL,
postal_code VARCHAR(30) NOT NULL,
phone INTEGER(10),
location VARCHAR(30) NOT NULL,
last_update VARCHAR(30) NOT NULL,
  PRIMARY KEY (id)
);

-- * 6a. Use `JOIN` to display the first and last names, as well as the address, 
-- of each staff member. Use the tables `staff` and `address`:

SELECT * FROM staff;
SELECT * FROM address;

SELECT first_name, last_name, address_id
FROM staff
JOIN address_id ON staff.address_id = address.address_id;

-- * 6b. Use `JOIN` to display the total amount rung up by each staff member in 
-- August of 2005. Use tables `staff` and `payment`.

SELECT payment.payment_date, payment.staff_id, payment.amount
FROM payment JOIN staff
ON payment.staff_id = staff.staff_id;

-- * 6c. List each film and the number of actors who are listed for that film. 
-- Use tables `film_actor` and `film`. Use inner join.

select * from film_actor;
select * from film;

SELECT film.film_id, film.title, film_actor.film_id, film_actor.actor_id
FROM film INNER JOIN film_actor 
ON film.film_id = film_actor.film_id;

-- * 6d. How many copies of the film `Hunchback Impossible` exist in the inventory system?

SELECT *
FROM film_actor
WHERE film_id IN
    (
        SELECT film_id
        FROM film
        WHERE title = 'HunchBack Impossible'
    );
    -- 
-- * 6e. Using the tables `payment` and `customer` and the `JOIN` command, list the total 
-- paid by each customer. List the customers alphabetically by last name:

select * from customer;
select * from payment;

SELECT payment.customer_id, payment.amount, customer.customer_id, customer.last_name
FROM payment JOIN customer
ON payment.customer_id = customer.customer_id;

-- * 7a. The music of Queen and Kris Kristofferson have seen an unlikely resurgence. 
-- As an unintended consequence, films starting with the letters `K` and `Q` have also soared in popularity. 
-- Use subqueries to display the titles of movies starting with the letters `K` and `Q` whose language is English. 

select * from film;

SELECT title
FROM film
WHERE title like 'Q%' or title like 'K%';

-- * 7b. Use subqueries to display all actors who appear in the film `Alone Trip`.

SELECT first_name, last_name
FROM actor
WHERE actor_id IN
    (
        SELECT actor_id
        FROM film_actor
        WHERE film_id in 
		(
			SELECT film_id
			FROM film
			WHERE title = 'Alone Trip'
		)
	);
    
-- * 7c. You want to run an email marketing campaign in Canada, 
-- for which you will need the names and email addresses of all Canadian customers. 
-- Use joins to retrieve this information.

SELECT country.country, country.last_update, customer.last_update, customer.email, customer.first_name, customer.last_name
FROM country JOIN customer
ON customer.last_update = country.last_update
where country.country = 'Canada';

-- * 7d. Sales have been lagging among young families, 
-- and you wish to target all family movies for a promotion. 
-- Identify all movies categorized as famiy films.

SELECT title
FROM film
WHERE film_id IN
    (
        SELECT film_id
        FROM film_category
        WHERE category_id in 
		(
			SELECT category_id
			FROM category
			WHERE name = 'family'
		)
	);

-- * 7e. Display the most frequently rented movies in descending order.

SELECT title 
FROM film_text 
WHERE film_id IN
    (
        SELECT film_id
        FROM inventory
        WHERE inventory_id in 
		(
			SELECT inventory_id
			rental
		)
        ORDER BY title desc
	);

-- * 7f. Write a query to display how much business, in dollars, each store brought in.
    
    SELECT s.store_id, SUM(amount) AS Gross
    FROM payment p
        JOIN rental r
            ON (p.rental_id = r.rental_id)
        JOIN inventory i
            ON (i.inventory_id = r.inventory_id)
        JOIN store s
            ON (s.store_id = i.store_id)
    GROUP BY s.store_id;

DROP VIEW total_sales;

-- * 7g. Write a query to display for each store its store ID, city, and country.

SELECT 
city.city, city.country_id, store.store_id, store.last_update,country.last_update,country.country
FROM store
    JOIN city
        ON city.last_update=store.last_update
     JOIN city
     ON city.last_update = country.last_update;

-- * 7h. List the top five genres in gross revenue in descending order. (**Hint**: you may need to use the following tables: 
-- category, film_category, inventory, payment, and rental.)

SELECT sum(amount)
FROM payment 
WHERE  rental_id IN
    (
        SELECT rental_id
        FROM rental
        WHERE inventory_id IN 
		(
			SELECT inventory_id
            FROM inventory
            WHERE film_id IN
            (
				SELECT film_id
                FROM film_category
                WHERE film_id IN
					(
						SELECT name
                        FROM category
                        group by name
					)
            )
		)
	)
	ORDER BY amount desc
    limit 5;


-- * 8a. In your new role as an executive, you would like to have an easy way of viewing the Top five genres by gross revenue. 
-- Use the solution from the problem above to create a view. If you haven't solved 7h, you can substitute another query to create a view.

CREATE VIEW top_five AS
	SELECT sum(amount)
FROM payment 
WHERE  rental_id IN
    (
        SELECT rental_id
        FROM rental
        WHERE inventory_id IN 
		(
			SELECT inventory_id
            FROM inventory
            WHERE film_id IN
            (
				SELECT film_id
                FROM film_category
                WHERE film_id IN
					(
						SELECT name
                        FROM category
                        group by name
					)
            )
		)
	)
	ORDER BY amount desc
    limit 5;

-- * 8b. How would you display the view that you created in 8a?

 SELECT * FROM top_five;
     
-- * 8c. You find that you no longer need the view `top_five_genres`. Write a query to delete it.

DROP VIEW top_five;
