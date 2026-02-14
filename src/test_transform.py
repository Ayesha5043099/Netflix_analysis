from config.config import DATA_PATH
from src.extract import load_csv
from src.transform import clean_movie_data

def test():
    # Load
    df = load_csv(DATA_PATH)

    # Clean
    df_clean = clean_movie_data(df)

    print("\n✅ Preview cleaned data:")
    print(df_clean.head())

    print("\n📊 Data types:")
    print(df_clean.dtypes)

    print("\n📈 Numeric summary:")
    print(df_clean[['gross', 'no_of_votes']].describe())

    # 🚨 Detect BIGINT overflow risks
    max_bigint = 9223372036854775807
    bad_gross = df_clean[df_clean['gross'] > max_bigint]

    if len(bad_gross) > 0:
        print("\n🚨 Gross values exceeding BIGINT:")
        print(bad_gross[['series_title', 'gross']])
    else:
        print("\n✅ No gross overflow detected")

    # 🚨 Detect INT overflow risks
    max_int = 2147483647
    bad_votes = df_clean[df_clean['no_of_votes'] > max_int]

    if len(bad_votes) > 0:
        print("\n🚨 Vote counts exceeding INT:")
        print(bad_votes[['series_title', 'no_of_votes']])
    else:
        print("\n✅ No vote overflow detected")


if __name__ == "__main__":
    test()