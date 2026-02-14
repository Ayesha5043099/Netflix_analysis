from config.config import DATA_PATH
from src.extract import load_csv
from src.transform import clean_movie_data
from src.load import (
    insert_movies,
    insert_directors,
    insert_genres,
    insert_actors,
    link_movie_directors,
    link_movie_genres,
    link_movie_actors
)


def test():

    print("📥 Loading CSV...")
    df = load_csv(DATA_PATH)
    print(f"✅ CSV loaded: {len(df)} rows")

    print("🧹 Cleaning data...")
    df_clean = clean_movie_data(df)
    print("✅ Data cleaning complete")

    print("💾 Inserting movies...")
    insert_movies(df_clean)

    print("🎬 Inserting directors...")
    insert_directors(df_clean)

    print("🏷 Inserting genres...")
    insert_genres(df_clean)

    print("🎭 Inserting actors...")
    insert_actors(df_clean)

    print("🔗 Linking movie-directors...")
    link_movie_directors(df_clean)

    print("🔗 Linking movie-genres...")
    link_movie_genres(df_clean)

    print("🔗 Linking movie-actors...")
    link_movie_actors(df_clean)

    print("\n🎉 PIPELINE COMPLETED SUCCESSFULLY 🎉")


if __name__ == "__main__":
    test()