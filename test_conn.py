from sqlalchemy import text
from load_data import engine

with engine.connect() as connection:

    result = connection.execute(text("""
        SELECT column_name, data_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
        AND table_name = 'event'
        ORDER BY ordinal_position
    """))

    print("Columns in event:")

    for row in result:
        print(f"- {row.column_name}: {row.data_type}")