DROP TABLE sales;
DROP TABLE books;
DROP TABLE authors;
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    first_name TEXT,
    last_name TEXT
);
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    author_id INTEGER REFERENCES authors(id)
);
CREATE TABLE sales (
    id SERIAL PRIMARY KEY,
    book_id INTEGER REFERENCES books(id),
    quantity INTEGER
);
INSERT INTO authors (first_name, last_name)
VALUES ('Igor', 'Petrov'),
    ('Dmitry', 'Sidorov'),
    ('Mark', 'Zuckerberg'),
    ('Vlad', 'Ivchik'),
    ('Max', 'Bobrov');
INSERT INTO books (title, author_id)
VALUES ('War and peace', 2),
    ('Garry Potter', 3),
    ('11 chairs', 1),
    ('Map', 5),
    ('Bibley', 2),
    ('Hermiona', 3),
    ('History', 1);

INSERT INTO books (title)
VALUES
('Hello world');

INSERT INTO sales (quantity, book_id)
VALUES (6, 2),
    (7, 1),
    (3, 3),
    (12, 6),
    (22, 5),
    (45, 7);
SELECT * FROM authors;

SELECT * FROM books;

SELECT * FROM sales;