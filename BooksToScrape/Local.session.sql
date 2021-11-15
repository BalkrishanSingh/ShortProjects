--@block
CREATE DATABASE scrape;

--@block
CREATE TABLE Books(
    Serial_no INT AUTO_INCREMENT,
    title VARCHAR(255), 
    book_url TINYTEXT,
    price VARCHAR(10),
    availability VARCHAR(25),
    PRIMARY KEY(Serial_no)
    );


--@block
-- DROP TABLE Books;

--@block
-- DESCRIBE Books;

--@block
CREATE UNIQUE INDEX Serial_Numbers ON Books (Serial_no);
--@block
SELECT *
FROM books;



