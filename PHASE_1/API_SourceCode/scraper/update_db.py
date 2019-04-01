import mysql.connector

def db_connect():
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
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
             "(type, date, number_affected) "
             "VALUES (%(type)s, %(date)s, %(number_affected)s)")
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
    count = 0
    for a in result:
        url_headline = {
            "url": a['url'],
            "headline": a['headline']
        }
        if search_article_url_headline(url_headline) == True:
            count += 1
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
                    "date": e['date'],
                    "number_affected": e['number-affected']
                }
                eid = add_event(event)
                evn_id.append(eid)
                
                location = {
                    "location_name": e['location']['country']
                }
                lid = search_location_name(location)
                if lid < 0:
                    print("adding")
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
    if count == len(result):
        return False
    return True

########################################################
# helper functions to get everything

# return list of reports for article with id=article_id
def get_article_reports(article_id):
    conn   = db_connect()
    cursor = conn.cursor(dictionary=True)
    one_cursor = conn.cursor()
    query  = ("SELECT * from Articles_Reports "
             "WHERE ar_article=" + article_id)
    reports_list = []
    try:
        cursor.execute(query)
        ar_reports = []
        for row in cursor:
            ar_reports.append(row)
        print(ar_reports)
        for ar_report in ar_reports:
            query = ("SELECT * from Reports "
                    "WHERE report_id=" + str(ar_report['ar_id']))
            cursor.execute(query)
            for row in cursor:
                row['disease'] = list(filter(None, row['disease'].split(',')))
                row['syndrome'] = list(filter(None, row['syndrome'].split(',')))
                report = row
                # each report has reported events
                query = ("SELECT * from Events_Reports "
                        "WHERE er_report=" + str(report['report_id']))
                cursor.execute(query)
                event_report_links = []
                report['reported_events'] = []
                for row in cursor:
                    event_report_links.append(row)
                # print(event_reports)
                for event_report_link in event_report_links:
                    event_id = str(event_report_link['er_event'])
                    # print(event_report)
                    query = ("SELECT el_location from Events_Locations "
                            "WHERE el_event=" + event_id)
                    one_cursor.execute(query)
                    location_id = one_cursor.fetchone()
                    location_id = location_id[0]
                    # print(location_id) 
                    query = ("SELECT * from Locations "
                            "WHERE location_id=" + str(location_id))
                    cursor.execute(query)
                    location = cursor.fetchone()
                   # print(event_report)

                    query = ("SELECT * from Events "
                            "WHERE event_id=" + event_id)
                    cursor.execute(query)
                    for row in cursor:
                        row['location'] = location
                        report['reported_events'].append(row)

                reports_list.append(report)
            
    except Exception as ex:
        print(ex)
    cursor.close()
    conn.close()
    return reports_list

########################################################

def search_article_id(article_id):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT * FROM Articles "
             "WHERE article_id=%s")
    res = None
    try:
        cursor.execute(query, (article_id,))
        for row in cursor:
            res = row
            if res:
                article_reports = get_article_reports(article_id)
                res['reports'] = article_reports
    except Exception as ex:
        print(ex)
    
    cursor.close()
    conn.close()

    return res

def search_by_date(start_date, end_date):
    conn   = db_connect()
    cursor = conn.cursor(dictionary=True)
    query  = ("SELECT article_id from Articles "
             "WHERE date_of_publication BETWEEN %s and %s") #how to search range???
    res = []
    try:
        cursor.execute(query, (start_date, end_date))
        for row in cursor:
            res.append(search_article_id(str(row['article_id'])))
        print(res)
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

def search_location_name(location):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT location_id FROM Locations "
             "WHERE location_name=%(location_name)s")
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

def search_article_url_headline(args):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("SELECT * FROM Articles "
             "WHERE url=%(url)s and headline=%(headline)s")
    try:
        cursor.execute(query, args)
        if cursor.rowcount > 0:
            return True
    except Exception as ex:
        print(ex)
    
    cursor.close()
    conn.close()
    return False

