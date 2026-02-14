SELECT title, gross
FROM movies
WHERE gross IS NOT NULL
ORDER BY gross DESC
LIMIT 10;