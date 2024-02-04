SELECT title, first_name, last_name FROM books
INNER JOIN authors ON authors.id = author_id;

SELECT first_name, last_name, title FROM authors
LEFT JOIN books ON authors.id = author_id;

SELECT title, first_name, last_name FROM authors
RIGHT JOIN books ON authors.id = author_id;