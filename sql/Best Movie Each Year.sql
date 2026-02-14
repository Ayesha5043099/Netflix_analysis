SELECT released_year, title, imdb_rating
FROM (
    SELECT 
        released_year,
        title,
        imdb_rating,
        RANK() OVER (PARTITION BY released_year ORDER BY imdb_rating DESC) rnk
    FROM movies
) t
WHERE rnk = 1;