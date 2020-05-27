Q1 = """select d.id, d.fname from 
        director d 
    WHERE EXISTS (
        SELECT  md.did
        FROM  moviedirector md 
        join movie m on m.id = md.mid
        join director di on md.did = di.id 
        WHERE year > 2000 and d.id = di.id
    ) AND NOT EXISTS (
        SELECT md.did 
        FROM  moviedirector md 
        join movie m on m.id = md.mid
        join director di on md.did = di.id
        where year < 2000 and d.id = di.id
    )
    group by d.id;""" 



Q3 = """SELECT di.fname,(
            SELECT m.name FROM director d 
            JOIN MovieDirector md ON md.did = d.id 
            JOIN movie m ON m.id = md.mid 
            WHERE d.id = di.id ORDER BY rank DESC LIMIT 1) AS name
            FROM director di LIMIT 100;"""



Q3 = """select * from actor 
         where not exists( 
         select ac.id from actor ac 
         join cast on ac.id = pid 
         join movie mv on mv.id = mid 
        where actor.id = ac.id and mv.year between 1990 and 2000)
        group by id order by id DESC limit 100; """