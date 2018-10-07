# Module to manupulate database
# Version: 1
# Date: 07.10.2018
# Time: 21:24 GMT+5

# IMPORTS
import sqlite3

# OPTIONS
database_name = 'database.db'

# FUNCTIONS
def create_base(database_name):
    # Creates base of a predesigned structure
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('''pragma foreign_keys = on''')
    c.execute('''CREATE TABLE Users (
            User_ID INTEGER PRIMARY KEY, 
            Username text
            )''')
    conn.commit()
    conn.close()

def nuke_base(database_name):
    # Wipes off created base
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('''pragma foreign_keys = on''')
    c.execute('''DROP TABLE Users''')
    conn.commit()
    conn.close()

# CODE

