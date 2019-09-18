# Module to manupulate database
# Version: 6
# Date: 18.09.2019
# Time: 23:06 GMT+5

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
            Username text NOT NULL UNIQUE
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

def create_user(username, database_name):
    # Creates a new user in the base
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('''INSERT INTO Users Values (null, ?)''', (username,))
    conn.commit()
    conn.close()

def delete_user(username, database_name):
    # deletes an existing user from the database
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('''pragma foreign_keys = on''')
    c.execute('''DELETE FROM Users
                    WHERE Username = ?''', (username,))
    conn.commit()
    conn.close()

def user_exists(username, database_name):
    # Searches for the user in the database, if he exists returns True otherwise - False
    conn = sqlite3.connect(database_name)
    c = conn.cursor()
    c.execute('''SELECT * FROM Users WHERE Username = ?''', (username,))
    output = c.fetchone()
    conn.commit()
    conn.close()
    if type(output) == type(()):
        return True
    else:
        return False

    
# CODE
if __name__ == '__main__':
    create_base(database_name)
