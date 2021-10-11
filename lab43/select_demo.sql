select fname, lname,birth_year from authors
	WHERE birth_year>1900;

# 'u' must be in fname AND lname:

 SELECT * from authors
 	WHERE fname LIKE 'kurt';

 SELECT * from authors
 	WHERE fname LIKE '%s';