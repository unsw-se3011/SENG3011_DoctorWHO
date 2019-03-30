import mysql.connector

def db_connect():
	mydb = mysql.connector.connect(
		host="localhost",
		user="cardis_db",
		passwd="password",
		database="DoctorWHO"
	)
	
	return mydb

def add_article(article):
    conn   = db_connect()
    cursor = conn.cursor()
    query  = ("INSERT INTO Articles "
             "(url, date_of_publication, headline, main_text, report_id) "
             "VALUES (%(url)s, %(date_of_publication)s, %(headline)s, %(main_text)s, %(report_id)d)")
    try:
        cursor.execute(query, article)
        print("Inserted article with id: " + str(cursor.lastrowid))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as ex:
        print(ex)

def add_report(report):
    conn   = db_connect()
    cursor = conn.cursor()
    query  = ("INSERT INTO Reports "
             "(disease, syndrome, comment, event_id) "
             "VALUES (%(disease)s, %(syndrome)s, %(comment)s, %(event_id)d)")
    try:
        cursor.execute(query, report)
        print("Inserted report with id: " + str(cursor.lastrowid))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as ex:
        print(ex)

def add_event(event):
    conn   = db_connect()
    cursor = conn.cursor()
    query  = ("INSERT INTO Events "
             "(type, date_of_event, number_affected, geonames_id) "
             "VALUES (%(type)s, %(date_of_event)s, %(number_affected)d, %(geonames_id)d)")
    try:
        cursor.execute(query, event)
        print("Inserted event with id: " + str(cursor.lastrowid))
        conn.commit()
        cursor.close()
        conn.close()
    except Exception as ex:
        print(ex)

