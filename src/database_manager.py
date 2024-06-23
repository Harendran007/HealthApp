import sqlite3

class DatabseService:
    def __init__(self, database):
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = sqlite3.connect(self.database)
            self.cursor = self.connection.cursor()
            print("Database Connection successful")
        except sqlite3.Error as e:
            print(f"Database Connection Failed: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            print("Connection to database closed")

    def drop_table(self, table_name):
        try:
            drop_tbl = f"DROP TABLE IF EXISTS {table_name}"
            self.cursor.execute(drop_tbl)
            print("Drop table successful")
        except sqlite3.Error as e:
            print(f"Dropping Table failed: {e}")

    def create_table(self, create_table_sql):
        try:
            self.cursor.execute(create_table_sql)
            print("Created table successful")
        except sqlite3.Error as e:
            print(f"Creating Table failed:: {e}")

    def insert_data(self, table_name, data):
        try:
            insert_query = f'INSERT INTO {table_name} VALUES ({",".join(["?" for _ in range(len(data[0]))])})'
            self.cursor.executemany(insert_query, data)
            self.connection.commit()
            print("Inserted data successfully")
        except Exception as e:
            print(f"Inserting data failed: {e}")
