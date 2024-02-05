CREATE TABLE Employees
(
    Name text,
    Position text,
    Departament text,
    Salary INT
);
INSERT INTO Employees (Name, Position, Departament, Salary)
VALUES ('Igor', 'Director', 'Marketing', 10000),
       ('Dima', 'Manager', 'Sales', 1000),
       ('Mark', 'Security', 'Defense', 1000);

UPDATE Employees
SET Position='Chief of sales'
WHERE name='Dima';

ALTER TABLE Employees
ADD COLUMN HireDate text DEFAULT NULL;

UPDATE Employees
SET HireDate='01.01.2023'
WHERE name='Igor';

UPDATE Employees
SET HireDate='01.01.2022'
WHERE name='Mark';

UPDATE Employees
SET HireDate='01.01.2021'
WHERE name='Dima';

SELECT name FROM Employees
WHERE Position='Manager';


SELECT name FROM Employees
WHERE Salary>5000;

SELECT name FROM Employees
WHERE Departament='Sales';

SELECT AVG(Salary)
FROM Employees;

DROP TABLE Employees;
