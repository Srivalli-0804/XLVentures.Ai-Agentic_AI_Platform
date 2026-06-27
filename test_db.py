from sqlalchemy import text

from backend.database.database import engine

with engine.connect() as conn:
    result = conn.execute(text("SELECT version();"))

    print(result.fetchone()[0])

print("Database connected successfully.")