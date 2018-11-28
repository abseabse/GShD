# Module to manupulate database
# Version: 3
# Date: 28.11.2018
# Time: 22:05 GMT+5

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
    c.execute('''CREATE TABLE Indicator_types (
            Type_ID INTEGER PRIMARY KEY,
            Type text
            )''')
    c.execute('''CREATE TABLE ActivitiesIndicators (
            Indicator_ID INTEGER PRIMARY KEY,
            Activity_ID integer,
            Indicator text,
            Type_ID text,
            FOREIGN KEY (Type_ID) REFERENCES Indicator_types(Type_ID)
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
if __name__ == '__main__':
    create_base(database_name)
