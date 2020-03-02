-- Number by score
-- Query that count the same score and order it in DESC
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER by number DESC;
