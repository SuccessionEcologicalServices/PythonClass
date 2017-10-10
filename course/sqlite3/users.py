# https://github.com/SuccessionEcologicalServices/PythonClass/blob/master/course/sqlite3.md

import sqlite3


FILENAME = "users.db"
TABLE_NAME = "users"

# Some default users
JENNY_DATA = [None, 'jennymc', '30', 'jenny', 'mccloud', 'blue']
JOE_DATA = [None, 'joewilson', '30', 'joe', 'wilson', 'yellow']

# Create connection to the database
with sqlite3.connect(FILENAME) as conn:

	# We will use the cursor object to perform transactions
	c = conn.cursor()

	# We can use {table} with the string function "format"
	# more here: https://docs.python.org/2/library/string.html#format-string-syntax
	INSERT_STATEMENT = "INSERT INTO {table} VALUES (?,?,?,?,?,?)" \
                       .format(table=TABLE_NAME)

	# execute the insert transaction
	# TODAY: add the correct variables for MY_LIST_X
	# OPTIONAL: try `execute many`
	#c.execute(INSERT_STATEMENT, JENNY_DATA)
	#c.execute(INSERT_STATEMENT, JOE_DATA)

	SELECT_STATEMENT = "SELECT * FROM {table}".format(table=TABLE_NAME)
	c.execute(SELECT_STATEMENT)
	print(c.fetchone())
	print(c.fetchone())
	print(c.fetchone())
	#print(c.fetchall())  # try this with fetchone commented out.

	# the above program prints all records in the database
	# can you write one which asks for an input color, and only
	# prints users who have that as a favorite?
	
	# tuples can be messy to work with - can you figure out how to
	# get the column names for each of the values we fetch?