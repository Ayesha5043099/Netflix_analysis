from src.db import get_connection

def test():
    conn = get_connection()
    print("✅ Database connected successfully!")
    conn.close()

if __name__ == "__main__":
    test()