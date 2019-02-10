# Version: 5
# Date: 11.02.2019
# Time: 02:38 GMT+5

# IMPORTS
import unittest
import sqlite3
import database_controller


# CREATING MOCK DATABASE FOR TEST PURPOSES
test_database = 'test_database.db'

# TODO decide, if I need this code:
# test_cursor = test_connection.cursor()
# test_cursor.execute('''pragma foreign_keys = on''')

# TEST BLOCK
# tests for database_controller.py

class Test_create_base(unittest.TestCase):
    # tests for create_base()
    
    def setUp(self):
        pass 

    def tearDown(self):
        database_controller.nuke_base(test_database)

    def test_one(self):
        # create base first time
        database_controller.create_base(test_database)
       
    def test_two(self):
        # try to create it two times in a row, should be an error
        database_controller.create_base(test_database)
        with self.assertRaises(sqlite3.OperationalError):
            database_controller.create_base(test_database)


class Test_nuke_base(unittest.TestCase):
    # tests for nuke_base()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_one(self):
        # try to nuke an existing base
        database_controller.create_base(test_database)
        database_controller.nuke_base(test_database)

    def test_two(self):
        # try to nuke an empty base, should not give an error
        database_controller.nuke_base(test_database)


class Test_create_base_table_tests(unittest.TestCase):
    # tests for tables structure

    def setUp(self):
        database_controller.create_base(test_database)

    def tearDown(self):
        database_controller.nuke_base(test_database)

    def test_one(self):
        # try to insert a value in table Users
        test_conn = sqlite3.connect(test_database)
        test_c = test_conn.cursor()
        test_c.execute('''pragma foreign_keys = on''')
        test_c.execute('''INSERT INTO Users VALUES (null, "goga")''')
        test_conn.commit()
        test_conn.close()

    def test_two(self):
        # try to insert two values in table Users
        test_conn = sqlite3.connect(test_database)
        test_c = test_conn.cursor()
        test_c.execute('''pragma foreign_keys = on''')
        test_c.execute('''INSERT INTO Users VALUES (null, "goga")''')
        test_c.execute('''INSERT INTO Users VALUES (null, "goga")''')
        test_conn.commit()
        test_conn.close()

    def test_three(self):
        # try to insert a value in table UsersActivities. Should be
        # an error, as the table has a foreign key in structure - User_ID
        # and we have not entered any Users yet
        with self.assertRaises(sqlite3.IntegrityError):
            test_conn = sqlite3.connect(test_database)
            test_c = test_conn.cursor()
            test_c.execute('''pragma foreign_keys = on''')
            test_c.execute('''INSERT INTO UsersActivities Values(
                null, 
                1, 
                "vopya"
                )''')
            test_conn.commit()
            test_conn.close()

    def test_four(self):
        # try to insert a pair of values in tables Users and UsersActivities. 
        # (testing foreign key constraint) Should not give an error.
        test_conn = sqlite3.connect(test_database)
        test_c = test_conn.cursor()
        test_c.execute('''pragma foreign_keys = on''')
        test_c.execute('''INSERT INTO Users Values(null, "goga")''')
        test_c.execute('''INSERT INTO UsersActivities Values(
            null, 
            1, 
            "vopya"
            )''')
        test_conn.commit()
        test_conn.close()

    def test_five(self):
        # try to insert two values in Indicator_types table.
        # Should not give an error.
        test_conn = sqlite3.connect(test_database)
        test_c = test_conn.cursor()
        test_c.execute('''pragma foreign_keys = on''')
        test_c.execute('''INSERT INTO Indicator_types Values(null, "date and time")''')
        test_c.execute('''INSERT INTO Indicator_types Values(null, "date and time")''')
        test_conn.commit()
        test_conn.close()

    def test_six(self):
        # try to insert a value in table ActivitiesIndicators without
        # appropriate values in foreign keys.
        # Should give an error.
        with self.assertRaises(sqlite3.IntegrityError):
            test_conn = sqlite3.connect(test_database)
            test_c = test_conn.cursor()
            test_c.execute('''pragma foreign_keys = on''')
            test_c.execute('''INSERT INTO ActivitiesIndicators Values (
                    null, 1, "goga", 2)''')
            test_conn.commit()
            test_conn.close()

    def test_seven(self):
        # try to insert a value in table ActivitiesIndicators with all the
        # other values in appropriate tables existing.
        # Should not give an error
        test_conn = sqlite3.connect(test_database)
        test_c = test_conn.cursor()
        test_c.execute('''pragma foreign_keys = on''')
        test_c.execute('''INSERT INTO Indicator_types Values (
                null, "chislo raz")''')
        test_c.execute('''INSERT INTO Users Values (null, "goga")''')
        test_c.execute('''INSERT INTO UsersActivities Values (
                null, 1, "ronyat kal")''')
        test_c.execute('''INSERT INTO ActivitiesIndicators Values (
                null, 1, "kak chasto", 1)''')
        test_conn.commit()
        test_conn.close()

    def test_eight(self):
        # try to insert a value in table IndicatorsValues without
        # an appropriate value in foreign key.
        # Should give an error.
        with self.assertRaises(sqlite3.IntegrityError):
            test_conn = sqlite3.connect(test_database)
            test_c = test_conn.cursor()
            test_c.execute('''pragma foreign_keys = on''')
            test_c.execute('''INSERT INTO IndicatorsValues Values (1, null, "5")''')
            test_conn.commit()
            test_conn.close()

    def test_nine(self):
        # try to insert an appropriate value in table IndicatorsValues with
        # all the other values in appropriate table existing.
        # Should not give an error.
        test_conn = sqlite3.connect(test_database)
        test_c = test_conn.cursor()
        test_c.execute('''pragma foreign_keys = on''')
        test_c.execute('''INSERT INTO Indicator_types Values (
                null, "chislo raz")''')
        test_c.execute('''INSERT INTO Users Values (null, "goga")''')
        test_c.execute('''INSERT INTO UsersActivities Values (
                null, 1, "ronyat kal")''')
        test_c.execute('''INSERT INTO ActivitiesIndicators Values (
                null, 1, "kak chasto", 1)''')
        test_c.execute('''INSERT INTO IndicatorsValues Values (1, null, 312)''')
        test_conn.commit()
        test_conn.close()


# MAIN CYCLE
if __name__ == '__main__':
    unittest.main()
