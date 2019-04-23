import mysql.connector

def db_connect():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="SIDRAT"
    )
    return conn

def add_user(user):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Users "
            "(username, password, email, name) "
            "VALUES (%(username)s, %(password)s, %(email)s, %(name)s) ")
    try:
        cursor.execute(query, user)
        insert_id = cursor.lastrowid
        print("Inserted user with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

def add_saved_article(article):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Articles "
            "(user_id, url) "
            "VALUES (%(user_id)s, %(url)s) ")
    try:
        cursor.execute(query, article)
        insert_id = cursor.lastrowid
        print("Inserted user with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

def remove_saved_article(article):
    pass

def add_subscription(subscription):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Subscriptions "
            "(user_id, url) "
            "VALUES (%(user_id)s, %(start_date)s, %(key_terms)s, %(location)s) ")
    try:
        cursor.execute(query, subscription)
        insert_id = cursor.lastrowid
        print("Inserted user with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

#####
def update_subscription():
    pass

def add_notification(article):
    conn   = db_connect()
    cursor = conn.cursor(buffered=True)
    query  = ("INSERT INTO Notifications "
            "(user_id, url) "
            "VALUES (%(user_id)s, %(url)s) ")
    try:
        cursor.execute(query, article)
        insert_id = cursor.lastrowid
        print("Inserted user with id: " + str(insert_id))
        conn.commit()
        cursor.close()
        conn.close()
        return insert_id
    except Exception as ex:
        print(ex)
        cursor.close()
        conn.close()
        return -1

def update_notification():
    pass
