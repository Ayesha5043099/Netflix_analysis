import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """
    Load CSV file into a Pandas DataFrame.

    Args:
        path (str): Path to CSV file

    Returns:
        pd.DataFrame
    """
    try:
        df = pd.read_csv(path)
        print(f" CSV loaded successfully: {len(df)} rows")
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f" File not found at path: {path}")
    except Exception as e:
        raise RuntimeError(f" Error loading CSV: {e}")