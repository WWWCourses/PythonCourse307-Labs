desc authors;

show CREATE TABLE authors;

-- TODO: check why error ?
select book_name FROM books WHERE books.author_id=authors.id;

ALTER TABLE authors ADD INDEX(fname(10));


use test;
show tables;

CREATE TABLE authors(
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	fname VARCHAR(20) DEFAULT NULL,
	lname VARCHAR(20) NOT NULL,
	UNIQUE( fname, lname)
);

desc authors;

INSERT INTO authors (fname,lname)
	VALUES
		('Kurt', "Vonnegut"),
		('Kurt', "FamilyName1"),
		('FirstName', "Vonnegut");

INSERT INTO authors (fname,lname)
	VALUES
		('Kurt', "Vonnegut");

