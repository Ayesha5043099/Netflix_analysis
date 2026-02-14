SELECT g.name, COUNT(*) AS movie_count
FROM genres g
JOIN movie_genres mg ON g.genre_id = mg.genre_id
GROUP BY g.name
ORDER BY movie_count DESC;