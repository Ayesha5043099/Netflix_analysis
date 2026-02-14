SELECT title, imdb_rating, no_of_votes
FROM movies
WHERE imdb_rating >= 8.5
AND no_of_votes < 50000
ORDER BY imdb_rating DESC;