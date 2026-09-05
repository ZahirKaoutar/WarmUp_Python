from sqlalchemy import create_engine, text

engine = create_engine(
    "postgresql://postgres:postgres@localhost:5432/exercices_db"
)

with engine.connect() as connection:
    result = connection.execute(text("SELECT * FROM clients"))

    for row in result:
        print(row)
