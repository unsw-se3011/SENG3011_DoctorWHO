import mysql.connector

def create_database():
	init_db = mysql.connector.connect(
		host="localhost",
		user="root",
		password="password"
	)

	init_cursor = init_db.cursor()

	init_cursor.execute("DROP DATABASE IF EXISTS SIDRAT")
	print("Old SIDRAT database removed (if it existed)")

	init_cursor.execute("CREATE DATABASE SIDRAT")
	print("SIDRAT database created")

def create_tables():
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		password="password",
        database="SIDRAT"
	)

	mycursor = mydb.cursor()
	mycursor.execute("DROP TABLE IF EXISTS Users")
	print("Old Users table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS Articles")
	print("Old Articles table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS Searches")
	print("Old Searches table removed (if it existed)")

	mycursor.execute("CREATE TABLE Users"
		" (user_id INT AUTO_INCREMENT PRIMARY KEY,"
		" username VARCHAR(255),"
		" password VARCHAR(255))")
	print("created Users table")

	mycursor.execute("CREATE TABLE Articles"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" user_id INT,"
		" article_id INT,"
		" FOREIGN KEY (user_id) REFERENCES Users(user_id))")
	print("created Articles table")

	mycursor.execute("CREATE TABLE Searches"
		" (id INT AUTO_INCREMENT PRIMARY KEY,"
		" user_id INT,"
		" start_date VARCHAR(255),"
		" end_date VARCHAR(255),"
		" key_term VARCHAR(255),"
		" location VARCHAR(255),"
		" FOREIGN KEY (user_id) REFERENCES Users(user_id))")
	print("created Searches table")

create_database()
create_tables()
