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

	mycursor.execute("DROP TABLE IF EXISTS Events")
	print("Old Events table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS Reports")
	print("Old Reports table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS ArticlesI")
	print("Old Articles table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS Locations")
	print("Old Locations table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS Events_Locations")
	print("Old Events_Locations table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS Events_Reports")
	print("Old Events_Reports table removed (if it existed)")
	mycursor.execute("DROP TABLE IF EXISTS Articles_Reports")
	print("Old Articles_Reports table removed (if it existed)")
	mycursor.execute("DROP VIEW IF EXISTS Events_Locations_summary;")
	print("Old Events_Locations_summary view removed (if it existed)")


	mycursor.execute("CREATE TABLE Events"
		" (event_id INT AUTO_INCREMENT PRIMARY KEY,"
		" type VARCHAR(255),"
		" date_of_event VARCHAR(255)," 
		" number_affected INT)")
	print("created Events table")

	mycursor.execute("CREATE TABLE Reports"
		" (report_id INT AUTO_INCREMENT PRIMARY KEY,"
		" disease VARCHAR(255),"
		" syndrome VARCHAR(255),"
		" comment VARCHAR(255))")
	print("created Reports table")

	mycursor.execute("CREATE TABLE Articles"
		" (articl_id INT AUTO_INCREMENT PRIMARY KEY,"
		" url VARCHAR(255),"
		" date_of_publication VARCHAR(255),"
		" headline VARCHAR(255),"
		" main_text VARCHAR(255)")
	print("created Articles table")

	mycursor.execute("CREATE TABLE Locations"
		" (location_id INT AUTO_INCREMENT PRIMARY KEY,"
		" location_name VARCHAR(255) PRIMARY KEY)")
	print("created Locations table")

	mycursor.execute("CREATE TABLE Events_Locations"
		" (el_id INT AUTO_INCREMENT PRIMARY KEY,"
		" el_event INT,"
		" el_location INT,"
		" FOREIGN KEY (el_event) REFERENCES Events(event_id),"
		" FOREIGN KEY (el_location) REFERENCES Locations(location_id)) ")
	print("created Events_Locations table")

	mycursor.execute("CREATE TABLE Events_Reports"
		" (er_id INT AUTO_INCREMENT PRIMARY KEY,"
		" er_event INT,"
		" er_report INT,"
		" FOREIGN KEY (er_event) REFERENCES Events(event_id),"
		" FOREIGN KEY (er_report) REFERENCES Reports(report_id))")
	print("created Events_Reports table")

	mycursor.execute("CREATE TABLE Articles_Reports"
		" (ar_id INT AUTO_INCREMENT PRIMARY KEY,"
		" ar_event INT,"
		" ar_article INT,"
		" FOREIGN KEY (ar_event) REFERENCES Events(event_id),"
		" FOREIGN KEY (ar_article) REFERENCES Articles(article_id))")
	print("created Articles_Reports table")
	
	mycursor.execute(
		"CREATE VIEW Events_Locations_Summary AS"
		  "SELECT"
		    "event_id AS els_event_id,"
		    "cast(concat('[', group_concat(json_quote(location_name) ORDER BY location_name SEPARATOR ','), ']') as json) AS els_location_name_array"
		  "FROM"
		    "Events"
		    "INNER JOIN Events_Locations"
		      "ON Events.event_id = Events_Locations.el_event"
		    "INNER JOIN fruit"
		      "ON Events_Locations.el_location = Locations.location_id"
		  "GROUP BY"
		    "event_id;")
	print("created Events_Locations_Summary view")

create_database()
create_tables()
