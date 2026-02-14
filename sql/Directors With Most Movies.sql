SELECT d.name, COUNT(*) AS movie_count
FROM directors d
JOIN movie_directors md ON d.director_id = md.director_id
GROUP BY d.name
ORDER BY movie_count DESC
LIMIT 10;