from config.config import DATA_PATH
from src.extract import load_csv

def test():
    df = load_csv(DATA_PATH)
    print(df.head())
    print("\nColumns:")
    print(df.columns.tolist())

if __name__ == "__main__":
    test()