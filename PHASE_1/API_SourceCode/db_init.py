import mysql.connector

def create_database():
	init_db = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password"
	)

	init_cursor = init_db.cursor()

	init_cursor.execute("DROP DATABASE IF EXISTS DoctorWHO")
	print("Old DoctorWHO database removed (if it existed)")

	init_cursor.execute("CREATE DATABASE DoctorWHO")
	print("DoctorWHO database created")

def create_tables():
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="password",
		database="DoctorWHO"
	)

	mycursor = mydb.cursor()

	mycursor.execute("CREATE TABLE Events (id INT AUTO_INCREMENT PRIMARY KEY, type VARCHAR(255), date_of_event VARCHAR(255), number_affected INT, geonames_id INT)")
	print("created Events table")
	mycursor.execute("CREATE TABLE Reports (id INT AUTO_INCREMENT PRIMARY KEY, disease VARCHAR(255), syndrome VARCHAR(255), comment VARCHAR(255), event_id INT, FOREIGN KEY (event_id) REFERENCES Events(id))")
	print("created Reports table")
	mycursor.execute("CREATE TABLE Articles (id INT AUTO_INCREMENT PRIMARY KEY, url VARCHAR(255), date_of_publication VARCHAR(255), headline VARCHAR(255), main_text VARCHAR(255),report_id INT, FOREIGN KEY (report_id) REFERENCES Reports(id))")
	print("created Articles table")

create_database()
create_tables()
