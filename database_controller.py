# Module to manupulate database
# Version: 4
# Date: 10.02.2019
# Time: 17:22 GMT+5

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
            Type_ID integer,
            FOREIGN KEY (Type_ID) REFERENCES Indicator_types(Type_ID),
            FOREIGN KEY (Activity_ID) REFERENCES UsersActivities(Activity_ID) 
            )''')
    c.execute('''CREATE TABLE IndicatorsValues (
            Indicator_ID integer,
            Time text,
            Value text,
            FOREIGN KEY (Indicator_ID) REFERENCES ActivitiesIndicators(Indicator_ID),
            PRIMARY KEY (Indicator_ID, Time)
            )''')
    conn.commit()
    conn.close()

def nuke_base(database_name):
    # Wipes off created base
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS UsersActivities''')
    c.execute('''DROP TABLE IF EXISTS Users''')
    c.execute('''DROP TABLE IF EXISTS ActivitiesIndicators''')
    c.execute('''DROP TABLE IF EXISTS IndicatorsValues''')
    c.execute('''DROP TABLE IF EXISTS Indicator_types''')
    conn.commit()
    conn.close()

# CODE
if __name__ == '__main__':
    create_base(database_name)
