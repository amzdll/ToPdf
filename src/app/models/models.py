from sqlalchemy import MetaData, Table, Column, Integer

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
)


# engine  = sqlalchemy.create_engine(DATABASE_URL)
# metadata.create_all(engine)
