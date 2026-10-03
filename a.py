"""
1) Add the lesson and activity details.
   a) Mention the lesson as "Basic SQL Statements".
   b) Mention the activity name as "Cricket Data Explorer".
   c) Mention the grade level.

2) Import the required libraries.
   a) Import `sqlite3` to create and manage the database.
   b) Import `pandas` as `pd` to display SQL results as tables.

3) Create and connect to the database.
   a) Create a database file named `cricket.db`.
   b) Create a cursor to run SQL commands.

4) Build the cricket tables.
   a) Remove old tables using `DROP TABLE IF EXISTS`.
   b) Create the `Team` table for team details.
   c) Create the `Match` table for match results.
   d) Create the `Player_Match` table for player match records.
   e) Insert sample cricket data into all tables.
   f) Use `commit()` to save the changes.

5) View database tables and match data.
   a) Use `sqlite_master` to display all tables in the database.
   b) Read the full `Match` table using `pd.read_sql()`.
   c) Use `.shape` to display the number of rows and columns.

6) Select rows and columns.
   a) Use `SELECT *` to fetch all columns from the Team table.
   b) Select only `Team_Id` and `Team_Name`.
   c) Select match and player IDs from the Player_Match table.

7) Filter data using `WHERE`.
   a) Find matches won by Rajasthan Royals.
   b) Use `AND` to combine conditions.
   c) Use `IN` to check multiple seasons.
   d) Find Mumbai Indians wins in Seasons 8 and 9.

8) Search team names using `LIKE`.
   a) Use `'De%'` to find team names starting with De.
   b) Use `'%Kings'` to find team names ending with Kings.

9) Find smallest and largest values.
   a) Use `MIN()` to find the smallest win margin.
   b) Use `MAX()` to find the largest win margin.
   c) Use `MIN()` and `MAX()` to find the earliest and latest seasons.

10) Close the database connection.
   a) Use `conn.close()` after completing all queries.
"""