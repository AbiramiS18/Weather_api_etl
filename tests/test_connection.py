from sqlalchemy import text
from app.db_connection import get_engine

try:
    engine = get_engine()

    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("✅ MySQL Connected Successfully")
        print(result.scalar())

except Exception as e:
    print("❌ Connection Failed")
    print(e)