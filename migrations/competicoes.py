
import sqlite3

# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('competicoes.db')

# cursor object
cursor_obj = connection_obj.cursor()

# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS COMPETICOES")

# Creating table
table = """CREATE TABLE competicoes (
            id INTEGER PRIMARY KEY,
            titulo VARCHAR(99) NOT NULL,
            data_fim TEXT
        )"""

cursor_obj.execute(table)

print("Table is Ready")

# Close the connection
connection_obj.close()
