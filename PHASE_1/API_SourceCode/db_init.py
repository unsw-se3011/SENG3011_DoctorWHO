import mysql.connector
from scraper import update_db

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
		" comment VARCHAR(2550))")
	print("created Reports table")

	mycursor.execute("CREATE TABLE Articles"
		" (article_id INT AUTO_INCREMENT PRIMARY KEY,"
		" url VARCHAR(255),"
		" date_of_publication VARCHAR(255),"
		" headline VARCHAR(255),"
		" main_text VARCHAR(2550))")
	print("created Articles table")

	mycursor.execute("CREATE TABLE Locations"
		" (location_id INT AUTO_INCREMENT PRIMARY KEY,"
		" location_name VARCHAR(255),"
		" geonames_id INT)")
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
		"CREATE VIEW Events_Locations_Summary AS "
		  "SELECT "
		    "event_id AS els_event_id, "
		    "cast(concat('[', group_concat(json_quote(location_name) ORDER BY location_name SEPARATOR ','), ']') as json) AS els_location_name_array "
		  "FROM "
		    "Events "
		    "INNER JOIN Events_Locations "
		      "ON Events.event_id = Events_Locations.el_event "
		    "INNER JOIN Locations "
		      "ON Events_Locations.el_location = Locations.location_id "
		  "GROUP BY "
		    "event_id;")
	print("created Events_Locations_Summary view")

def add_example():
    articles = [
        {
            "id": "0", # this field was added
            "url":"www.who.int/lalala",
            "date_of_publication":"2018-12-12Txx:xx:xx",
            "headline":"Outbreaks in Southern Vietnam",
            "main_text":"Three people infected by what is thought to be H5N1 or H7N9 in Ho Chi Minh city. First infection occurred on 1 Dec 2018, and latest is report on 10 December. Two in hospital, one has recovered. Furthermore, two people with fever and rash infected by an unknown disease.",
            "reports":[
                {
                    "id":0,
                    "disease":[
                        "influenza a/h5n1",
                        "influenza a/h7n9" 
                    ],
                    "syndrome":[
                    ],
                    "reported_events":[
                        {
                            "id": 0,
                            "type":"recovered",
                            "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                            "location":{
                                "geonames-id":1566083
                            },
                            "number-affected":1 
                        },
                        {
                            "id": 1,
                            "type":"hospitalised",
                            "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                            "location":{
                                "geonames-id":1566083 },
                            "number-affected":2
                        }
                    ],
                    "comment":None
                },
                {
                    "id":1,
                    "disease":[
                        "unknown"
                    ],
                    "syndrome":[
                        "Acute fever and rash"
                    ],
                    "reported_events":[
                        {
                            "id": 2,
                            "type":"infected",
                            "date":"2018-12-01Txx:xx:xx to 2018-12-10Txx:xx:xx",
                            "location":{
                                "geonames-id":1566083
                            },
                            "number-affected":2
                        }
                    ],
                    "comment":None
                }
            ]
        }
    ]
    
    art_id = []
    for a in articles:
        article = {
            "url": a['url'],
            "date_of_publication": a['date_of_publication'],
            "headline": a['headline'],
            "main_text": a['main_text']
        }
        aid = update_db.add_article(article)
        art_id.append(aid)
        
        rep_id = []
        for r in a['reports']:
            report = {
                "disease": ','.join(r['disease']),
                "syndrome": ','.join(r['syndrome']),
                "comment": r['comment']
            }
            rid = update_db.add_report(report)
            rep_id.append(rid)
            
            evn_id = []
            for e in r['reported_events']:
                event = {
                    "type": e['type'],
                    "date_of_event": e['date'],
                    "number_affected": e['number-affected']
                }
                eid = update_db.add_event(event)
                evn_id.append(eid)
                
                location = {
                    "location_name": None,
                    "geonames_id": e['location']['geonames-id']
                }
                lid = update_db.search_location(location)
                if lid < 0:
                    lid = update_db.add_location(location)
                
                event_location = {
                    "event_id": eid,
                    "location_id": lid
                }
                update_db.add_event_location(event_location)
                
                event_report = {
                    "event_id": eid,
                    "report_id": rid
                }
                update_db.add_event_report(event_report)
                
                article_report = {
                    "event_id": eid,
                    "article_id": aid
                }
                update_db.add_article_report(article_report)

create_database()
create_tables()
add_example()
