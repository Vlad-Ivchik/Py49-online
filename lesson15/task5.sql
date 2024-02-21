SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS all_sales
FROM authors
INNER JOIN books ON authors.id = books.author_id
INNER JOIN sales ON books.id = sales.book_id
GROUP BY authors.first_name, authors.last_name
HAVING SUM(sales.quantity) = (
    SELECT MAX(all_sales)
    FROM (
        SELECT SUM(sales.quantity) AS all_sales
        FROM authors
        INNER JOIN books ON authors.id = books.author_id
        INNER JOIN sales ON books.id = sales.book_id
        GROUP BY authors.first_name, authors.last_name
    )
);



SELECT first_name, last_name, title, quantity FROM authors
INNER JOIN books ON books.author_id = authors.id
INNER JOIN sales ON sales.book_id = books.id
WHERE sales.quantity > (SELECT AVG(sales.quantity) FROM sales);


SELECT first_name, last_name, AVG(quantity) FROM authors
INNER JOIN books ON books.author_id = authors.id
INNER JOIN sales ON sales.book_id = books.id
GROUP BY authors.first_name, authors.last_name
HAVING AVG(sales.quantity) > (SELECT AVG(sales.quantity) FROM sales)