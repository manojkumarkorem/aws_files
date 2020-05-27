Q1 = """
    SELECT DISTINCT p.player_id, p.team_id, p.jersey_no, p.name, p.date_of_birth, p.age 
    FROM Player p
    LEFT JOIN MatchCaptain mc ON mc.captain = p.player_id
    LEFT JOIN GoalDetails gd ON gd.team_id = p.team_id
    WHERE mc.captain NOT IN(
        SELECT DISTINCT gd1.player_id 
        FROM GoalDetails gd1 
    );
"""

Q2 = """
    SELECT DISTINCT team_id, COUNT() AS no_of_games 
    FROM MatchCaptain
    GROUP BY team_id;
"""

Q3 = """
    SELECT p.team_id, (COUNT(goal_id)/23.0)AS avg_goal_score 
    FROM Player p
    INNER JOIN GoalDetails gd ON gd.player_id = p.player_id
    GROUP BY P.team_id;
"""

Q4 = """
    SELECT captain, COUNT() AS no_of_times_captain
    FROM MatchCaptain mc
    GROUP BY captain;
"""

Q5 = """
   SELECT COUNT() AS no_players
   FROM Player p 
   WHERE (SELECT captain 
        FROM MatchCaptain mc
        INNER JOIN player p1 ON mc.captain = p1.player_id
        INNER JOIN Match m ON m.match_no = mc.match_no
        WHERE m.player_of_match = mc.captain AND p.player_id = p1.player_id
    );
"""

Q6 = """
    SELECT DISTINCT p.player_id AS no_players
    FROM Player p 
    WHERE p.player_id IN (SELECT captain 
        FROM MatchCaptain)
        AND p.player_id NOT IN (SELECT 
        player_of_match FROM Match);
"""

Q7 = """
    SELECT strftime('%m',m.play_date), COUNT() AS no_of_matches 
    FROM Match m
    GROUP BY strftime('%m',m.play_date)
    ORDER BY no_of_matches DESC;
"""

Q8 = """
    SELECT p.jersey_no, COUNT() AS no_captains 
    FROM Player p
    INNER JOIN MatchCaptain mc ON mc.captain = p.player_id
    GROUP BY p.jersey_no
    ORDER BY no_captains DESC, p.jersey_no DESC;
"""

Q9 = """
    SELECT p.player_id, AVG(audience) AS avg_audience
    FROM Match m
    INNER JOIN MatchTeamDetails mtd ON mtd.match_no = m.match_no
    INNER JOIN Player p ON p.team_id = mtd.team_id
    GROUP BY p.player_id
    ORDER BY avg_audience DESC, p.player_id DESC;
"""

Q10 = """
    SELECT p.team_id, AVG(p.age)
    FROM Player p
    GROUP BY p.team_id;
"""

Q11 = """
    SELECT AVG(p.age) AS avg_age_of_captains
    From Player P
    INNER JOIN MatchCaptain mc ON mc.captain = p.player_id;
"""

Q12 = """
    SELECT strftime('%m',p.date_of_birth) AS month, COUNT() AS no_of_players
    FROM Player p
    GROUP BY strftime('%m',p.date_of_birth)
    ORDER BY no_of_players DESC, strftime('%m',p.date_of_birth) DESC;
"""

Q13 = """
    SELECT mc.captain, COUNT() AS no_of_wins
    FROM MatchCaptain mc
    INNER JOIN MatchTeamDetails mtd ON mtd.match_no = mc.match_no
    WHERE mtd.win_lose = 'W' AND mc.team_id = mtd.team_id
    GROUP BY mc.captain
    ORDER BY no_of_wins DESC;
"""