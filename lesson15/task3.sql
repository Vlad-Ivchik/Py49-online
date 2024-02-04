SELECT title, first_name, last_name, quantity
FROM books
INNER JOIN authors
    ON authors.id = author_id
INNER JOIN sales
    ON books.id=book_id;


SELECT first_name, last_name, title, quantity
FROM authors
    LEFT JOIN books ON authors.id = author_id
    LEFT JOIN sales ON books.id = book_id;