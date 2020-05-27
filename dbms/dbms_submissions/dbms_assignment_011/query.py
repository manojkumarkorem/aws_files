Q1 = """
    SELECT a.id, a.fname, a.lname, a.gender 
    FROM actor a
    INNER JOIN cast c ON c.pid = a.id
    INNER JOIN movie m ON m.id = c.mid
    WHERE m.name LIKE 'annie%';
"""

Q2 = """
    SELECT m.id,m.name,m.rank,m.year from movie m
    INNER JOIN MovieDirector md ON md.mid = m.id
    INNER JOIN Director d ON d.id = md.did
    where (d.fname = 'Biff' and d.lname = 'Malibu') and m.year in (1999, 1994, 2003)
    order by m.rank DESC, m.year ASC;
"""

Q3 = """
    SELECT m.year,COUNT() AS no_of_movies
    FROM movie m
    GROUP BY m.year
    HAVING AVG(m.rank) > (SELECT AVG(mo.rank) FROM movie mo)
    ORDER BY m.year ASC;
"""

Q4 = """
    SELECT m.id, m.name, m.year, m.rank
    FROM Movie m
    WHERE m.year = 2001 AND m.rank < (SELECT AVG(m1.rank) 
                                       FROM movie m1) 
    ORDER BY m.rank DESC
    LIMIT 10;
"""

Q5 = """
    SELECT c.mid, COUNT( case when a.gender ='F'
            then 1 end ) as Female
        ,COUNT( case when a.gender ='M'
            then 1 end ) as Male
    FROM actor a 
    INNER JOIN cast c on c.pid = a.id
    GROUP BY c.mid
    ORDER BY c.mid ASC 
    LIMIT 100;
"""

Q6 = """
    SELECT DISTINCT a.id
    FROM actor a
    INNER JOIN cast c on c.pid = a.id
    INNER JOIN movie m ON m.id = c.mid
    GROUP BY m.id,c.pid
    HAVING COUNT(DISTINCT c.role) > 1
    ORDER BY c.pid ASC
    LIMIT 100;
"""

Q7 = """
    SELECT d1.fname,COUNT() as count_of_same_fname_dire
    FROM Director d1
    GROUP BY d1.fname
    HAVING count_of_same_fname_dire > 1;
"""

Q8 = """
    SELECT d.id, d.fname, d.lname 
    FROM director d
    WHERE d.id IN (
	SELECT d.id
	FROM director d
	INNER JOIN moviedirector md ON md.did = d.id
	INNER JOIN cast c ON c.mid = md.mid
	GROUP BY c.mid,d.id
	HAVING COUNT(DISTINCT c.pid ) >= 100
	)
    AND d.id NOT IN(
	SELECT d.id
	FROM director d
	INNER JOIN moviedirector md ON md.did = d.id
	INNER JOIN cast c ON c.mid = md.mid
	GROUP BY c.mid,d.id
	HAVING COUNT(DISTINCT c.pid ) < 100
	);
"""