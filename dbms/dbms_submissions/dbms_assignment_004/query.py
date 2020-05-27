Q1 = "SELECT COUNT(*) FROM Movie WHERE year = 2002 AND rank > 2 AND NAME LIKE 'Ha%';"

Q2 = "SELECT MAX(rank) FROM Movie WHERE (year = 1983 or year = 1994) AND NAME LIKE 'Autom%';"

Q3 = "SELECT COUNT(*) FROM Actor WHERE gender = 'M' AND (fname LIKE '%ei' or lname LIKE 'ei%');"

Q4 = "SELECT AVG(rank) AS average_rank_of_movies FROM Movie WHERE year IN (1993, 1995, 2000) AND rank >= 4.2;"

Q5 = "SELECT SUM(rank) FROM Movie WHERE year BETWEEN 1981 and 1984 AND rank < 9 and name LIKE '%Hary%';"

Q6 = "SELECT year FROM Movie WHERE rank = 5 LIMIT 1;"

Q7 = "SELECT COUNT(*) FROM Actor WHERE gender = 'F' or fname = lname;"

Q8 = "SELECT DISTINCT(fname) FROM Actor WHERE lname LIKE '%ei' ORDER BY fname ASC LIMIT 100"

Q9 = "SELECT ID, name AS movie_title, year FROM Movie WHERE year IN (2001, 2002, 2005, 2006) LIMIT 25 OFFSET 10;"

Q10 = "SELECT DISTINCT(lname) FROM Director WHERE fname IN ('Yeud', 'Wolf', 'Vicky') ORDER BY lname LIMIT 5;"