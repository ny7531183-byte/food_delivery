# #pip insatll -r requirements.txt

import pandas as pd
from sqlalchemy import create_engine


def connect_database():
    try:
        engine = create_engine(
            "mysql+pymysql://root:root@localhost:3306/food_delivery"
        )

        # Test the database connection
        with engine.connect():
            pass

        return engine, True

    except Exception as e:
        print(f"Database connection failed: {e}")
        return None, False


def connect_tables():
    engine, connected = connect_database()

    if not connected or engine is None:
        raise ConnectionError("MySQL database connection failed.")

    try:
        customers = pd.read_sql_query(
            "SELECT * FROM customers", engine
        )

        menu_item = pd.read_sql_query(
            "SELECT * FROM Menu_item", engine
        )

        orders = pd.read_sql_query(
            "SELECT * FROM Orders", engine
        )

        rest = pd.read_sql_query(
            "SELECT * FROM Restaurants", engine
        )

        delivery = pd.read_sql_query(
            "SELECT * FROM Delivery", engine
        )

        return customers, menu_item, orders, rest, delivery

    except Exception as e:
        print(f"Error loading tables: {e}")
        raise


# Test manually only when running this file directly
if __name__ == "__main__":
    tables = connect_tables()
    print("All tables loaded successfully.")
    for table in tables:
        print(table.shape)
