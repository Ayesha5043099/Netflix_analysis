SELECT DISTINCT a.name, m.title, m.imdb_rating
FROM movies m
JOIN movie_actors ma ON m.movie_id = ma.movie_id
JOIN actors a ON ma.actor_id = a.actor_id
WHERE m.imdb_rating >= 9.0
ORDER BY m.imdb_rating DESC;