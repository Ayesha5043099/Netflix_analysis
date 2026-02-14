from psycopg2.extras import execute_values
from src.db import get_connection
import numpy as np


# --------------------------------------------------
# INSERT MOVIES
# --------------------------------------------------
def insert_movies(df):

    df = df.replace({np.nan: None})

    query = """
        INSERT INTO movies (
            title,
            released_year,
            certificate,
            runtime_min,
            imdb_rating,
            meta_score,
            no_of_votes,
            gross,
            overview,
            poster_link
        )
        VALUES %s
        ON CONFLICT DO NOTHING;
    """

    values = df[[
        'series_title',
        'released_year',
        'certificate',
        'runtime_min',
        'imdb_rating',
        'meta_score',
        'no_of_votes',
        'gross',
        'overview',
        'poster_link'
    ]].values.tolist()

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                execute_values(cur, query, values)

        print(f"✅ Inserted {len(values)} movies")

    finally:
        conn.close()


# --------------------------------------------------
# INSERT DIRECTORS
# --------------------------------------------------
def insert_directors(df):

    directors = set()

    for director_list in df['director'].dropna():
        for director in director_list.split(","):
            directors.add((director.strip(),))

    query = """
        INSERT INTO directors (name)
        VALUES %s
        ON CONFLICT DO NOTHING;
    """

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                execute_values(cur, query, list(directors))

        print(f"✅ Inserted {len(directors)} directors")

    finally:
        conn.close()


# --------------------------------------------------
# INSERT GENRES
# --------------------------------------------------
def insert_genres(df):

    genres = set()

    for genre_list in df['genre'].dropna():
        for genre in genre_list.split(","):
            genres.add((genre.strip(),))

    query = """
        INSERT INTO genres (name)
        VALUES %s
        ON CONFLICT DO NOTHING;
    """

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                execute_values(cur, query, list(genres))

        print(f"✅ Inserted {len(genres)} genres")

    finally:
        conn.close()


# --------------------------------------------------
# INSERT ACTORS
# --------------------------------------------------
def insert_actors(df):

    actors = set()

    for col in ['star1', 'star2', 'star3', 'star4']:
        for actor in df[col].dropna():
            actors.add((actor.strip(),))

    query = """
        INSERT INTO actors (name)
        VALUES %s
        ON CONFLICT DO NOTHING;
    """

    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cur:
                execute_values(cur, query, list(actors))

        print(f"✅ Inserted {len(actors)} actors")

    finally:
        conn.close()


# --------------------------------------------------
# LINK MOVIE ↔ DIRECTORS
# --------------------------------------------------
def link_movie_directors(df):

    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cur:

                for _, row in df.iterrows():

                    cur.execute(
                        "SELECT movie_id FROM movies WHERE title = %s",
                        (row['series_title'],)
                    )
                    movie = cur.fetchone()

                    if not movie:
                        continue

                    movie_id = movie[0]

                    if row['director']:
                        for director in row['director'].split(","):

                            cur.execute(
                                "SELECT director_id FROM directors WHERE name = %s",
                                (director.strip(),)
                            )
                            director_record = cur.fetchone()

                            if director_record:
                                director_id = director_record[0]

                                cur.execute(
                                    """
                                    INSERT INTO movie_directors (movie_id, director_id)
                                    VALUES (%s, %s)
                                    ON CONFLICT DO NOTHING;
                                    """,
                                    (movie_id, director_id)
                                )

        print("✅ Linked movie-directors")

    finally:
        conn.close()


# --------------------------------------------------
# LINK MOVIE ↔ GENRES
# --------------------------------------------------
def link_movie_genres(df):

    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cur:

                for _, row in df.iterrows():

                    cur.execute(
                        "SELECT movie_id FROM movies WHERE title = %s",
                        (row['series_title'],)
                    )
                    movie = cur.fetchone()

                    if not movie:
                        continue

                    movie_id = movie[0]

                    if row['genre']:
                        for genre in row['genre'].split(","):

                            cur.execute(
                                "SELECT genre_id FROM genres WHERE name = %s",
                                (genre.strip(),)
                            )
                            genre_record = cur.fetchone()

                            if genre_record:
                                genre_id = genre_record[0]

                                cur.execute(
                                    """
                                    INSERT INTO movie_genres (movie_id, genre_id)
                                    VALUES (%s, %s)
                                    ON CONFLICT DO NOTHING;
                                    """,
                                    (movie_id, genre_id)
                                )

        print("✅ Linked movie-genres")

    finally:
        conn.close()


# --------------------------------------------------
# LINK MOVIE ↔ ACTORS
# --------------------------------------------------
def link_movie_actors(df):

    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cur:

                for _, row in df.iterrows():

                    cur.execute(
                        "SELECT movie_id FROM movies WHERE title = %s",
                        (row['series_title'],)
                    )
                    movie = cur.fetchone()

                    if not movie:
                        continue

                    movie_id = movie[0]

                    for col in ['star1', 'star2', 'star3', 'star4']:

                        actor_name = row[col]

                        if actor_name:
                            cur.execute(
                                "SELECT actor_id FROM actors WHERE name = %s",
                                (actor_name.strip(),)
                            )
                            actor_record = cur.fetchone()

                            if actor_record:
                                actor_id = actor_record[0]

                                cur.execute(
                                    """
                                    INSERT INTO movie_actors (movie_id, actor_id)
                                    VALUES (%s, %s)
                                    ON CONFLICT DO NOTHING;
                                    """,
                                    (movie_id, actor_id)
                                )

        print("✅ Linked movie-actors")

    finally:
        conn.close()