Q1 = """SELECT COUNT(*) 
        FROM Movie 
        WHERE year < 2000;
        """

Q2 = """SELECT AVG(rank) 
        FROM Movie 
        WHERE year = 1991;
        """

Q3 = """SELECT MIN(rank) 
        FROM Movie 
        WHERE year = 1991;
        """

Q4 = """SELECT fname,lname 
        FROM actor 
        INNER JOIN cast ON pid = id 
        WHERE mid = 27;
        """

Q5 = """select count(id) 
        from actor 
        inner join cast on id = pid 
        where fname = 'Jon' AND lname = 'Dough';
        """


Q6 = """select name 
        from movie 
        where name LIKE 'Young Latin Girls%' and year between 2003 and 2006
        """

Q7 = """select fname,lname 
        from director 
        inner join MovieDirector on director.id = moviedirector.did 
        inner join movie on mid = movie.id
        where movie.name LIKE 'Star Trek%'
        GROUP BY did
        having count(mid) >= 1;
        """

Q8 = """select name 
        from movie 
        inner join cast on `cast`.mid = `movie`.id 
        inner join MovieDirector on `MovieDirector`.mid = `movie`.id
        inner join actor on `actor`.id = `cast`.pid 
        inner join director on `director`.id = `moviedirector`.did  
        where (actor.fname = 'Jackie (I)' and actor.lname = 'Chan') and (director.fname = 'Jackie (I)' and director.lname = 'Chan');
        """

Q9 = """select fname,lname 
        from director 
        inner join MovieDirector on director.id = moviedirector.did 
        inner join movie on mid = movie.id  
        where year = 2001 
        GROUP BY did 
        having count(mid) >= 4 
        ORDER BY fname ASC, lname DESC;
        """

Q10 = """SELECT gender, COUNT(id) 
         FROM Actor 
         GROUP BY gender;
         """

Q11 = """select mv1.name,mv2.name,mv1.rank,mv1.year
         from movie as mv1 
         cross join movie as mv2
         where mv1.rank = mv2.rank 
         GROUP BY mv2.name,mv1.name
         limit 100;
         """

Q12 = """select fname,movie.year,movie.rank
         from actor 
         inner join cast on `cast`.pid = `actor`.id
         inner join movie on `cast`.mid =`movie`.id 
         ORDER BY fname ASC,year DESC 
         limit 100;
         """




Q13 = """select actor.fname,director.fname,AVG(rank) as score
         from movie 
         inner join cast on `cast`.mid = `movie`.id
         inner join MovieDirector on `MovieDirector`.mid = `movie`.id 
         inner join actor on `actor`.id = `cast`.pid 
         inner join director on `director`.id = `moviedirector`.did
         group by `MovieDirector`.did,`actor`.id 
         having count(`moviedirector`.mid)>=5 
         order by score DESC,`actor`.id ASC 
         limit 100;
         """