Q1 = "SELECT fname, lname FROM Actor INNER JOIN Cast ON pid = id WHERE mid = 12148;"


Q2 = "SELECT COUNT(id) FROM Actor INNER JOIN Cast ON pid = id  WHERE fname = 'Harrison (I)' AND lname = 'Ford';"



Q3 = "SELECT DISTINCT(pid) FROM Cast INNER JOIN Movie ON mid = id WHERE Movie.name LIKE 'Young Latin Girls%';"


Q4 = "SELECT COUNT(DISTINCT(pid)) FROM Cast INNER JOIN Movie ON mid = id WHERE Movie.year BETWEEN 1990 AND 2000;"

