/* -------------------------- show all mysql users -------------------------- */
SELECT * FROM mysql.user;

/* ---------------------------- show table schema --------------------------- */
DESC employees;

/* --------------------------- show george salary --------------------------- */
SELECT first_name, salary
FROM employees, salaries
WHERE
	employees.first_name="George" AND
	employees.emp_no=salaries.emp_no
ORDER BY salaries.salary
LIMIT 100;

