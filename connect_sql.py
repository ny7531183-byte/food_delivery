#pip insatll -r requirements.txt

import pandas as pd
from sqlalchemy import create_engine

def connect_database():
   try:
        engine= create_engine(url="mysql+mysqldb://root:root@localhost/food_delivery")
   except:
        print("Connection Failed")
   else:
        return engine

if connect_database():
   print("Database Connected successfully")

def  connect_tables():
    try:
        customers=pd.read_sql_query("select * from customers;",connect_database())
        menu_item=pd.read_sql_query("select * from Menu_item;",connect_database())
        orders=pd.read_sql_query("select * from Orders;",connect_database())
        rest=pd.read_sql_query("select * from Restaurants;",connect_database())
        delivery=pd.read_sql_query("select * from Delivery;",connect_database())
        print(customers)
    except:
        print("Table Name is incorrect..check once")
    else:
         return customers,menu_item,orders,rest,delivery

print(connect_tables())


   
# from sqlalchemy import create_engine, text

# engine = create_engine(
#     "mysql+pymysql://root:root@localhost:3306/food_delivery"
# )

# with engine.connect() as connection:
#     result = connection.execute(text("SHOW TABLES"))

#     for table in result:
#         print(table[0])

# from sqlalchemy import text

# with engine.connect() as connection:
#     result = connection.execute(text("SELECT * FROM customers LIMIT 10"))

#     for row in result:
#         print(row)