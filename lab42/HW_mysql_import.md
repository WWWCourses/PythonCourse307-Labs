# Task

1. Download file: <a id="raw-url" href="https://raw.githubusercontent.com/WWWCourses/PythonCourse307-Labs/main/lab42/books_db_dump.sql" download="books_db_dump.sql" target="_blank">books_db_dump.sql</a>
2. Import the 'books_db_dump.sql' into your MySQL instance, which should create the database 'books_db'
3. List all tables into 'books_db'

	*Expected results*

	| Tables_in_books_db   |
	|----------------------|
	| authors              |
	| books                |

5. Execute next select statement:
   `SELECT * FROM books LIMIT 5;`

   *Expected results:*

	|   id |   author_id | book_name           |   pub_year |
	|------|-------------|---------------------|------------|
	|    1 |           1 | The Sirens of Titan |       1959 |
	|    2 |           1 | Mother Night        |       1961 |
	|    3 |           1 | Cat's Cradle        |       1963 |
	|    4 |           1 | God Bless You       |       1965 |
	|    5 |           1 | Slaughterhouse      |       1969 |
