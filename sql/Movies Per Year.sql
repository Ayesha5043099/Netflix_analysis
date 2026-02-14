SELECT released_year, COUNT(*) AS total_movies
FROM movies
GROUP BY released_year
ORDER BY released_year;