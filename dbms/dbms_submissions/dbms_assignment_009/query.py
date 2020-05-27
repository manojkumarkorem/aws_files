Q1 = """
    SELECT AVG(age)
    FROM Player;
"""
Q2 = """
    SELECT match_no,
        play_date
    FROM Match
    WHERE audience > 50000
    ORDER BY match_no ASC;
"""
Q3 ="""
    SELECT team_id,
        COUNT(team_id) AS mat 
    FROM MatchTeamDetails
    GROUP BY team_id,win_lose
    HAVING win_lose = 'W'
    ORDER BY mat DESC,team_id ASC;
"""

Q4 ="""
    SELECT match_no,
        play_date
    FROM Match
    WHERE stop1_sec > (SELECT AVG(stop1_sec) FROM Match)
    ORDER BY match_no DESC;
"""
Q5 = """
    SELECT mc.match_no,t.name,p.name
    FROM Team AS t 
        INNER JOIN MatchCaptain AS mc 
            On t.team_id = mc.team_id 
        INNER JOIN Player AS p 
            ON p.player_id = mc.captain
    ORDER BY mc.match_no ASC,t.name ASC;  
"""
Q6 = """
    SELECT m.match_no,p.name,p.jersey_no 
    FROM Match AS m
        INNER JOIN Player AS p
            ON p.player_id = m.player_of_match
    ORDER BY m.match_no ASC;
"""
Q7 = """
    SELECT t.name,AVG(p.age) AS avr 
    FROM Player AS p 
        INNER JOIN Team AS t 
            ON p.team_id = t.team_id                                                                           
    GROUP BY p.team_id
    HAVING avr >26
    ORDER BY t.name ASC;
"""
Q8 ="""
    SELECT p.name,p.jersey_no,p.age,COUNT(gd.goal_id) AS no_goals
    FROM GoalDetails AS gd
        INNER JOIN Player AS p
            ON gd.player_id = p.player_id
    GROUP BY gd.player_id
    HAVING no_goals >=1 AND p.age <=27
    ORDER BY no_goals DESC,p.name ASC;
"""
Q9 = """
   SELECT team_id,
        (100.0 * COUNT(goal_id) /(SELECT COUNT(goal_id) FROM GoalDetails)) AS percentage 
    FROM GoalDetails
   GROUP BY team_id
   HAVING percentage > 0;
"""
Q10 ="""
    SELECT AVG(avr) AS total_avg 
    FROM(
        SELECT COUNT(goal_id) AS avr 
        FROM GoalDetails
        GROUP BY team_id
    );
"""
Q11 = """
    SELECT player_id,
        name,
        date_of_birth  
    FROM Player
    WHERE player_id NOT IN(SELECT DISTINCT player_id FROM GoalDetails)
    ORDER BY player_id ASC;
"""

Q12 = """
    SELECT t.name, m.match_no, m.audience, m.audience - (SELECT AVG(audience) FROM match join matchcaptain mc on mc.match_no = match.match_no join team te on mc.team_id = te.team_id where te.team_id = t.team_id) as diff_btw_avg_audience
    FROM match m
    INNER JOIN matchcaptain mc
        ON m.match_no = mc.match_no
    INNER JOIN team t
        ON mc.team_id = t.team_id
    ORDER BY m.match_no ASC;
"""