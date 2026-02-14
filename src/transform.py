import pandas as pd

def clean_movie_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )

    # Runtime
    if 'runtime' in df.columns:
        df['runtime_min'] = (
            df['runtime']
            .astype(str)
            .str.extract(r'(\d+)')
        )
        df['runtime_min'] = pd.to_numeric(df['runtime_min'], errors='coerce')

    # Gross
    if 'gross' in df.columns:
        df['gross'] = (
            df['gross']
            .astype(str)
            .str.replace(",", "", regex=False)
            .str.replace("$", "", regex=False)
            .str.strip()
        )
        df['gross'] = pd.to_numeric(df['gross'], errors='coerce')

        max_bigint = 9223372036854775807
        df.loc[df['gross'] > max_bigint, 'gross'] = None
        df.loc[df['gross'] > 1_000_000_000_000, 'gross'] = None

    # Numeric conversions
    numeric_cols = [
        'released_year',
        'imdb_rating',
        'meta_score',
        'no_of_votes'
    ]

    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # ✅ Prevent INT overflow for votes
    if 'no_of_votes' in df.columns:
        max_int = 2147483647
        df.loc[df['no_of_votes'] > max_int, 'no_of_votes'] = None

    # Fill missing categorical
    if 'certificate' in df.columns:
        df['certificate'] = df['certificate'].fillna("Unrated")

    if 'director' in df.columns:
        df['director'] = df['director'].fillna("Unknown")

    print("✅ Data cleaning complete")

    return df