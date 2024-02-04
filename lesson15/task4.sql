SELECT first_name, last_name, sum(quantity)
FROM authors
INNER JOIN books ON books.author_id = authors.id
INNER JOIN sales ON sales.book_id = books.id
GROUP BY authors.first_name, authors.last_name;


SELECT first_name, last_name, sum(quantity)
FROM authors
LEFT JOIN books ON books.author_id = authors.id
LEFT JOIN sales ON sales.book_id = books.id
GROUP BY authors.first_name, authors.last_name;