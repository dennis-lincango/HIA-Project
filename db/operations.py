import pandas as pd
from sqlalchemy import create_engine, text
from config.config import CONNECTION_STRING


# Función para crear la tabla
def create_table_electronics():
    engine = create_engine(CONNECTION_STRING)
    with engine.connect() as conn:
        conn.execute(text("""
            IF NOT EXISTS (
                SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME = 'ElectronicsDatabaseData'
            )
            BEGIN
                CREATE TABLE ElectronicsDatabaseData (
                    id INT PRIMARY KEY,
                    [prices.amountMax] FLOAT,
                    [prices.amountMin] FLOAT,
                    [prices.availability] NVARCHAR(100),
                    [prices.isSale] BIT,
                    [prices.merchant] NVARCHAR(255),
                    [prices.shipping] NVARCHAR(100),
                    Brand NVARCHAR(100),
                    categories NVARCHAR(255),
                    name NVARCHAR(255),
                    weight NVARCHAR(50)
                )
            END
        """))


# Función para insertar los datos obtenidos de Faker
def insert_data(df: pd.DataFrame):
    engine = create_engine(CONNECTION_STRING)
    df = df.where(pd.notnull(df), None)
    df.to_sql('ElectronicsDatabaseData', engine, if_exists='append', index=False)
