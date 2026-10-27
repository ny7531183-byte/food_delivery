# # import pandas as pd
# # from connect_sql import connect_tables

# # def load_data():
# #     tables=connect_tables()

# #     tablenames=['Customers','Menu','Orders','Rest','Delivery']
# #     i=0

# #     for table in tables:
# #         table.to_csv(f"Data_SQL/{tablenames[i]}.csv")
# #         i+=1
# #     data={}
# #     i=0
# #     for table in tablenames:
# #         data[table]= tables[i]
# #         i=i+1
# #     return data
# # # print(load_data())

# # def clean_data(df=pd.DataFrame()):
# #     null_values=df.isnull().sum()
   
# #     df.dropna(inplace=True)
# #     df.drop_duplicates(inplace=True)
# #     for col in df.select_dtypes(include='object').columns:
# #         df[col]=df[col].str.strip()
# #         df[col]=df[col].str.lower()
# #     return df 


# # def load_clean_data():
# #     data=load_data()
# #     clean_df={}

# #     for table_name,table_data in data.items():
# #         clean_df[table_name]=clean_data(table_data)

# #     return clean_df

# # load_clean_data 

# import pandas as pd
# from pathlib import Path
# from connect_sql import connect_tables

# def load_data():
#     tables = connect_tables()

#     tablenames = [
#         'customers',
#         'menu_item',
#         'orders',
#         'rest',
#         'delivery'
#     ]

#     # Check that 5 tables were returned
#     if len(tables) != len(tablenames):
#         raise ValueError(
#             f"Expected 5 tables, but received {len(tables)}"
#         )

#     # Create Data_SQL folder if it doesn't exist
#     output_dir = Path("Data_SQL")
#     output_dir.mkdir(parents=True, exist_ok=True)

#     data = {}

#     for name, table in zip(tablenames, tables):
#         if not isinstance(table, pd.DataFrame):
#             raise TypeError(f"{name} is not a pandas DataFrame")

#         file_path = output_dir / f"{name}.csv"

#         table.to_csv(file_path, index=False)
#         data[name] = table

#         print(f"Saved: {file_path.resolve()} | Rows: {len(table)}")

#     return data


# def clean_data(df):
#     df = df.copy()
#     df.dropna(inplace=True)
#     df.drop_duplicates(inplace=True)

#     for col in df.select_dtypes(include='object').columns:
#         df[col] = df[col].str.strip().str.lower()

#     return df


# def load_clean_data():
#     data = load_data()
#     clean_df = {}

#     for table_name, table_data in data.items():
#         clean_df[table_name] = clean_data(table_data)

#     return clean_df


# if __name__ == "__main__":
#     tables = connect_tables()
#     print("Delivery rows:", len(tables[4]))
#     print(tables[4].head())



import pandas as pd
from pathlib import Path
from connect_sql import connect_tables

# Always use the project folder as the base directory
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "Data_SQL"

TABLE_NAMES = [
    "Customers",
    "Menu",
    "Orders",
    "Rest",
    "Delivery"
]


def load_data():
    # Fetch tables from MySQL
    tables = connect_tables()

    if len(tables) != len(TABLE_NAMES):
        raise ValueError(
            f"Expected {len(TABLE_NAMES)} tables, "
            f"but received {len(tables)}"
        )

    # Create output folder if it doesn't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    data = {}

    for name, df in zip(TABLE_NAMES, tables):
        if not isinstance(df, pd.DataFrame):
            raise TypeError(f"{name} is not a DataFrame")

        # Save original data to CSV
        file_path = OUTPUT_DIR / f"{name}.csv"
        df.to_csv(file_path, index=False, encoding="utf-8-sig")

        data[name] = df.copy()

        print(f"Saved: {file_path}")
        print(f"Rows: {len(df)}, Columns: {len(df.columns)}")

    print("\nAll original CSV files saved successfully!")
    return data


def clean_data(df):
    # Do not modify the original DataFrame
    df = df.copy()

    # Remove duplicate rows
    df.drop_duplicates(inplace=True)

    # Clean text columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].apply(
            lambda value: value.strip() if isinstance(value, str)
            else value
        )

    # Drop rows that are completely empty
    df.dropna(how="all", inplace=True)

    return df


def load_clean_data():
    data = load_data()
    clean_df = {}

    for table_name, table_data in data.items():
        cleaned = clean_data(table_data)
        clean_df[table_name] = cleaned

        # Save cleaned data separately
        file_path = OUTPUT_DIR / f"{table_name}_cleaned.csv"
        cleaned.to_csv(
            file_path,
            index=False,
            encoding="utf-8-sig"
        )

        print(f"Cleaned CSV saved: {file_path}")
        print(f"Cleaned rows: {len(cleaned)}")

    print("\nAll original and cleaned CSV files saved!")
    return clean_df


if __name__ == "__main__":
    try:
        cleaned_data = load_clean_data()

        print("\nDelivery table preview:")
        print(cleaned_data["Delivery"].head())

    except Exception as error:
        print(f"\nError: {error}")
        raise

    