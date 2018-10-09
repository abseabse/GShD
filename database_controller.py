# Module to manupulate database
# Version: 2
# Date: 09.10.2018
# Time: 23:34 GMT+5

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
    c.execute('''CREATE TABLE UsersActivities (
            Activity_ID INTEGER PRIMARY KEY,
            User_ID integer,
            Activity text,
            FOREIGN KEY (User_ID) REFERENCES Users(User_ID)
            )''')
    conn.commit()
    conn.close()

def nuke_base(database_name):
    # Wipes off created base
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS UsersActivities''')
    c.execute('''DROP TABLE IF EXISTS Users''')
    conn.commit()
    conn.close()

# CODE

