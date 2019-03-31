import mysql.connector

def db_connect():
	mydb = mysql.connector.connect(
		host="localhost",
		user="cardis_db",
		passwd="password",
		database="DoctorWHO"
	)
	
	return mydb

# Insert new article into database
def add_article(article):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Articles "
             "(url, date_of_publication, headline, main_text) "
             "VALUES (%(url)s, %(date_of_publication)s, %(headline)s, %(main_text)s)")
    try:
        cursor.execute(query, article)
        insert_id = cursor.lastrowid
        print("Inserted article with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

# Insert new report into database
def add_report(report):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Reports "
             "(disease, syndrome, comment) "
             "VALUES (%(disease)s, %(syndrome)s, %(comment)s)")
    try:
        cursor.execute(query, report)
        insert_id = cursor.lastrowid
        print("Inserted report with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

# Insert new event into database
def add_event(event):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Events "
             "(type, date_of_event, number_affected) "
             "VALUES (%(type)s, %(date_of_event)s, %(number_affected)s)")
    try:
        cursor.execute(query, event)
        insert_id = cursor.lastrowid
        print("Inserted event with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

# Insert new location into database
def add_location(location):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Locations "
             "(location_name, geonames_id) "
             "VALUES (%(location_name)s, %(geonames_id)s)")
    try:
        cursor.execute(query, location)
        insert_id = cursor.lastrowid
        print("Inserted location with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

# Insert new location link for event into database
def add_event_location(event_location):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Events_Locations "
             "(el_event, el_location) "
             "VALUES (%(event_id)s, %(location_id)s)")
    try:
        cursor.execute(query, event_location)
        insert_id = cursor.lastrowid
        print("Inserted event_location with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

# Insert new event link for report into database
def add_event_report(event_report):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Events_Reports "
             "(er_event, er_report) "
             "VALUES (%(event_id)s, %(report_id)s)")
    try:
        cursor.execute(query, event_report)
        insert_id = cursor.lastrowid
        print("Inserted event_report with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

# Insert new report link for article into database
def add_article_report(article_report):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Articles_Reports "
             "(ar_event, ar_article) "
             "VALUES (%(event_id)s, %(article_id)s)")
    try:
        cursor.execute(query, article_report)
        insert_id = cursor.lastrowid
        print("Inserted article_report with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

def add_result(result):
    art_id = []
    for a in result:
        if a == [] or search_article_url(a['url']) == True:
            continue
        article = {
            "url": a['url'],
            "date_of_publication": a['date_of_publication'],
            "headline": a['headline'],
            "main_text": a['main_text']
        }
        aid = add_article(article)
        art_id.append(aid)
        
        rep_id = []
        for r in a['reports']:
            report = {
                "disease": ','.join(r['disease']),
                "syndrome": ','.join(r['syndrome']),
                "comment": r['comment']
            }
            rid = add_report(report)
            rep_id.append(rid)
            
            evn_id = []
            for e in r['reported_events']:
                event = {
                    "type": e['type'],
                    "date_of_event": e['date'],
                    "number_affected": e['number-affected']
                }
                eid = add_event(event)
                evn_id.append(eid)
                
                location = {
                    "location_name": e['location']['country'],
                    "geonames_id": e['location']['geonames-id']
                }
                lid = search_location(location)
                if lid < 0:
                    lid = add_location(location)
                
                event_location = {
                    "event_id": eid,
                    "location_id": lid
                }
                add_event_location(event_location)
                
                event_report = {
                    "event_id": eid,
                    "report_id": rid
                }
                add_event_report(event_report)
                
                article_report = {
                    "event_id": eid,
                    "article_id": aid
                }
                add_article_report(article_report)
    
    print("Have added these articles: ")
    print(art_id)

########################################################

def search_article_id(article_id):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT * FROM Articles "
             "WHERE article_id=%s")
    res = None
    try:
        cursor.execute(query, (article_id,))
        if cursor.rowcount > 0:
            for row in cursor:
                res = row
    except Exception as ex:
        print(ex)
    
    cursor.close()
    conn.close()
    return res

def search_pub_date(pub_date):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT * FROM Articles "
             "WHERE date_of_publication=%s") #how to search range???
    res = []
    try:
        cursor.execute(query, (pub_date,))
        if cursor.rowcount > 0:
            for row in cursor:
                res.append(row)
    except Exception as ex:
        print(ex)
    
    cursor.close()
    conn.close()
    return res
"""
def search_report(report):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT location_id from Locations "
             "WHERE geonames_id=%(geonames_id)s or location_name=%(location_name)s")
    res = -1
    try:
        cursor.execute(query, location)
        if cursor.rowcount > 0:
            for (location_id,) in cursor:
                res = int(location_id)
    except Exception as ex:
        print(ex)
    
    cursor.close()
    conn.close()
    return res

def search_event(event):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT location_id from Locations "
             "WHERE geonames_id=%(geonames_id)s or location_name=%(location_name)s")
    res = -1
    try:
        cursor.execute(query, location)
        if cursor.rowcount > 0:
            for (location_id,) in cursor:
                res = int(location_id)
    except Exception as ex:
        print(ex)
    
    cursor.close()
    conn.close()
    return res
"""
def search_location(location):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT location_id FROM Locations "
             "WHERE geonames_id=%(geonames_id)s OR location_name=%(location_name)s")
    res = -1
    try:
        cursor.execute(query, location)
        if cursor.rowcount > 0:
            for (location_id,) in cursor:
                res = int(location_id)
    except Exception as ex:
        print(ex)
    
    cursor.close()
    conn.close()
    return res

def search_article_url(url):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT * FROM Articles "
             "WHERE url=%s")
    try:
        cursor.execute(query, (url,))
        if cursor.rowcount > 0:
            return True
    except Exception as ex:
        print(ex)
    
    cursor.close()
    conn.close()
    return False

