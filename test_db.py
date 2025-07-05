import os
import psycopg
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Print environment variables
print("Environment variables:")
print(f"DB_HOST: {os.getenv('DB_HOST')}")
print(f"DB_PORT: {os.getenv('DB_PORT')}")
print(f"DB_USER: {os.getenv('DB_USER')}")
print(f"DB_PASSWORD: {os.getenv('DB_PASSWORD')}")
print(f"DB_DATABASE: {os.getenv('DB_DATABASE')}")

# Test connection
try:
    conn_str = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}"
    print(f"\nConnection string: {conn_str}")
    conn = psycopg.connect(conn_str)
    print("✓ Database connection successful")
    conn.close()
except Exception as e:
    print(f"✗ Database connection failed: {e}")
